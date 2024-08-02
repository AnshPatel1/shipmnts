from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=1024)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(default="admin@vedanya.com", unique=True)
    full_name = models.CharField(max_length=1024)
    roles = models.ManyToManyField(Role, null=True, blank=True)
    supervisor = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['full_name', 'email']

    def __str__(self):
        return self.username


class CustomUserManager(BaseUserManager):
    def create_user(self, username, full_name, is_staff, is_admin, password='12345678'):
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            username=username,
            full_name=full_name
        )
        user.full_name = full_name
        user.is_staff = is_staff
        user.is_admin = is_admin
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, full_name, password=None):
        user = self.create_user(
            password=password,
            full_name=full_name,
            username=username
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
