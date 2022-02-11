from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from ..mixins import TimestampMixin

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, is_staff=False, is_admin=False, is_active=True):
        if not username:
            raise ValueError('username is required')
        if not email:
            raise ValueError('email is required')
        if not password:
            raise ValueError('password is required')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.is_staff = is_staff
        user.is_admin = is_admin
        user.is_active = is_active

        user.save(using=self._db)
        return user

    def create_staffuser(self, username, email, password=None):
        user = self.create_user(
            username,
            email,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            username,
            email,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user


class User(AbstractBaseUser, TimestampMixin, PermissionsMixin):
    email = models.EmailField(unique=True, blank=False)
    first_name = models.CharField(max_length=64, blank=True, null=True)
    last_name = models.CharField(max_length=64, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    def __str__(self):
        return str(f"{self.username}::{self.email}")

    class Meta:
        ordering = ('username', 'email','last_name', 'first_name', )

    
    def has_perm(self, perm: str, obj=None) -> bool:
        return True

    def has_module_perms(self, app_label: str) -> bool:
        return True