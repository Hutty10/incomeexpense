from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not username:
            raise ValueError(_("User Should have a username"))
        if not email:
            raise ValueError(_("User Should have an Email"))
        if password is None:
            raise ValueError(_("Password is compulsory"))

        user = self.model(
            email=self.normalize_email(email), username=username, **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_verified", True)
        extra_fields.setdefault("is_active", True)
        if not extra_fields.get("is_staff"):
            raise ValueError(_("staff must be set to true"))
        if not extra_fields.get("is_superuser"):
            raise ValueError(_("Superuser must be set to true"))
        user = self.create_user(
            username=username, email=email, password=password, **extra_fields
        )
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, db_index=True, max_length=254)
    username = models.CharField(unique=True, db_index=True, max_length=50)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = UserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self) -> str:
        return self.email

    def tokens(self) -> dict:
        tokens = RefreshToken.for_user(self)
        return {"refresh": str(tokens), "access": str(tokens.access_token)}
