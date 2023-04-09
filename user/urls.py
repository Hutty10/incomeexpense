from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from user.views import LoginView, RegisterView, VerifyEmail,SetNewPasswordAPIView,PasswordTokenCheckAPI,RequestPasswordResetEmailView

app_name = "user"


urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("email-verify/", VerifyEmail.as_view(), name="email_verify"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('request-reset-email/', RequestPasswordResetEmailView.as_view(),
         name="request-reset-email"),
    path('password-reset/<uidb64>/<token>/',
         PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    path('password-reset-complete', SetNewPasswordAPIView.as_view(),
         name='password-reset-complete')
]
