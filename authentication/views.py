from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegistrationSerializer, UserLoginSerializer, OTPVerificationSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import ListAPIView
from django.core.cache import cache
from datetime import timedelta
from django.utils.timezone import now

# User Registration View
class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': {
                    'email': user.email,
                    'phone': user.phone,
                    'first_name': user.first_name,
                    'last_name': user.last_name
                },
                'otp': user.otp,  # Send OTP for verification
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# User Login View
class UserLoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        user_type = 'user'  # Default user type
        if email:
            user = CustomUser.objects.filter(email=email).first()
            if user:
                user_type = user.user_type

        cache_key = f"login_attempts_{email}"
        lock_key = f"login_lock_{email}"

        # Check if the user is locked
        if cache.get(lock_key):
            lock_duration = "30 minutes" if user_type == 'admin' else "10 minutes"
            return Response(
                {"error": f"Too many failed attempts. Try again after {lock_duration}."},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            # Reset failed attempts on successful login
            cache.delete(cache_key)
            return Response(serializer.validated_data, status=status.HTTP_200_OK)

        # Increment failed attempts on invalid login
        attempts = cache.get(cache_key, 0) + 1
        cache.set(cache_key, attempts, timeout=1800)  # Cache for 30 minutes

        # Lock the user if attempts exceed the limit
        if (user_type == 'admin' and attempts >= 3) or (user_type == 'user' and attempts >= 3):
            lock_duration = 1800 if user_type == 'admin' else 600  # 30 min for admin, 10 min for user
            cache.set(lock_key, True, timeout=lock_duration)
            lock_message = "30 minutes" if user_type == 'admin' else "10 minutes"
            return Response(
                {"error": f"Too many failed attempts. Login suspended for {lock_message}."},
                status=status.HTTP_403_FORBIDDEN
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# OTP Verification View
class OTPVerificationView(APIView):
    def post(self, request):
        serializer = OTPVerificationSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Admin User List View
class AdminUserListView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [IsAdminUser]
