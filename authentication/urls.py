from django.urls import path
from .views import UserRegistrationView, UserLoginView, OTPVerificationView, AdminUserListView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('verify-otp/', OTPVerificationView.as_view(), name='otp-verify'),
    path('users/', AdminUserListView.as_view(), name='admin-user-list'),
]
