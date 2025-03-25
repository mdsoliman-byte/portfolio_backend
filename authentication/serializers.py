from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken

# User Registration Serializer
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = CustomUser
        fields = ('email', 'phone', 'password', 'first_name', 'last_name')

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            phone=validated_data['phone'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        user.generate_otp()  # Generate an OTP for verification
        return user

# User Login Serializer
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)

            if user:
                if not user.is_active:
                    raise serializers.ValidationError("User account is disabled.")

                # Generate JWT Tokens
                refresh = RefreshToken.for_user(user)
                return {
                    'user': {
                        'email': user.email,
                        'phone': user.phone,
                        'first_name': user.first_name,
                        'last_name': user.last_name
                    },
                    'access_token': str(refresh.access_token),
                    'refresh_token': str(refresh)
                }
            else:
                raise serializers.ValidationError("Unable to log in with provided credentials.")
        else:
            raise serializers.ValidationError("Must include 'email' and 'password'.")

# OTP Verification Serializer
class OTPVerificationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)

    def validate(self, data):
        email = data.get('email')
        otp = data.get('otp')

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError("User not found.")

        if user.otp != otp:
            raise serializers.ValidationError("Invalid OTP.")

        user.otp = None  # Clear OTP after successful verification
        user.save()
        return {"message": "OTP verified successfully!"}
