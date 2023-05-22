from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from accounts.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model.
    """

    email = models.EmailField(
        _('email address'),
        max_length=100,
        unique=True,
    )
    username = models.CharField(
        _('username'),
        max_length=100,
        unique=True,
    )
    first_name = models.CharField(
        _('first name'),
        max_length=30,
    )
    last_name = models.CharField(
        _('last name'),
        max_length=30,
    )

    is_active = models.BooleanField(
        _('active'),
        default=True,
    )
    is_verified = models.BooleanField(
        _('verified'),
        default=False,
    )
    is_superuser = models.BooleanField(
        _('superuser'),
        default=False,
    )
    is_staff = models.BooleanField(
        _('staff'),
        default=False,
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username',
        'first_name',
        'last_name',
    ]

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')


def get_default_profile_image() -> str:
    return 'default/default_profile_image.jpg'


def get_default_profile_banner() -> str:
    return 'default/default_profile_banner.jpg'


def get_profile_image_upload_path(instance: 'Profile', filename: str) -> str:
    return f'upload/users/{instance.user.email}/profile_image/{filename}'


def get_profile_banner_upload_path(instance: 'Profile', filename: str) -> str:
    return f'upload/users/{instance.user.email}/profile_banner/{filename}'


class Profile(models.Model):
    """
    Profile for user.
    """

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    user: User = models.OneToOneField(
        User,
        related_name='profile',
        on_delete=models.CASCADE,
    )
    profile_image = models.ImageField(
        verbose_name='user profile image',
        blank=True,
        null=True,
        upload_to=get_profile_image_upload_path,
        default=get_default_profile_image,
    )
    profile_banner = models.ImageField(
        verbose_name='user profile banner',
        blank=True,
        null=True,
        upload_to=get_profile_banner_upload_path,
        default=get_default_profile_banner,
    )
    gender = models.CharField(
        verbose_name='user gender',
        blank=True,
        null=True,
        max_length=2,
        choices=GENDER_CHOICES,
    )
    description = models.TextField(
        verbose_name='user profile description',
        blank=True,
        null=True,
        max_length=500,
    )

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'

    def __str__(self):
        return f'Profile for {self.user}'
