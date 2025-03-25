from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.db import models
from django.core.validators import RegexValidator
from django.apps import apps
import random

# Custom User Manager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, phone, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        if not phone:
            raise ValueError("Users must have a phone number")

        extra_fields.setdefault('is_admin', False)
        extra_fields.setdefault('is_staff', False)
        email = self.normalize_email(email)
        user = self.model(email=email, phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone, password=None):
        user = self.create_user(email, phone, password, is_admin=True, is_staff=True)
        user.save(using=self._db)
        return user

# Custom User Model
class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True) 
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True, validators=[RegexValidator(r'^[0-9]{10,15}$')])
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    otp = models.CharField(max_length=6, blank=True, null=True)

    groups = models.ManyToManyField(
        Group,
        related_name="customuser_set",  # Unique related_name
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_set",  # Unique related_name
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']

    def __str__(self):
        return self.email

    def generate_otp(self):
        self.otp = str(random.randint(100000, 999999))
        self.save()
        return self.otp

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if apps.is_installed('rest_framework.authtoken'):  # Check if authtoken app is installed
            from rest_framework.authtoken.models import Token
            if not Token.objects.filter(user=self).exists():  # Ensure token creation only if it doesn't exist
                Token.objects.create(user=self)
