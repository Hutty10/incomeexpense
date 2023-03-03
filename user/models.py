from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if username is None:
            raise TypeError("User Should have a username")
        if email is None:
            raise TypeError("User Should have an Email")

        user = self.model(
            username=username, email=self.normalize_email(email), **extra_fields
        )
        user.set_password(password)
        user.save()


def create_superuser(self, email, username, password=None, **extra_fields):
    extra_fields.setdefault("is_staff", True)
    extra_fields.setdefault("is_superuser", True)
    if not extra_fields.get("is_staff"):
        raise ValueError(_("staff must be set to true"))
    if not extra_fields.get("is_superuser"):
        raise ValueError(_("Superuser must be set to true"))
    user = self.create_user(email, username, password, **extra_fields)
    return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, db_index=True, max_length=50)
    email = models.EmailField(unique=True, db_index=True, max_length=254)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = UserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        return ""
