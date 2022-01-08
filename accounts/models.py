from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from model_location.models import City


# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, first_name, phone_number, password=None, **extra_fields):
        if not first_name:
            raise ValueError('The name is required')

        if not phone_number:
            raise ValueError('Phone number is required')

        user = self.model(
            first_name=first_name,
            phone_number=phone_number,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, first_name, phone_number, password):
        user = self.create_user(
            first_name=first_name,
            phone_number=phone_number,
            password=password
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=255, unique=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, related_name='users', null=True, blank=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name']

    objects = UserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        full_name = f'{self.first_name} {self.phone_number}'
        return full_name.strip()

    def __str__(self) -> str:
        return self.get_full_name()

    def has_perm(self, perm, obj=None) -> bool:
        return self.is_admin

    def has_module_perms(self, app_label) -> bool:
        return True
