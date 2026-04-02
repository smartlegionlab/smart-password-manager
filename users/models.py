from datetime import timedelta

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.cache import cache
from django.db import models
from django.templatetags.static import static
from django.utils import timezone

from django.utils.functional import cached_property

from users.managers.custom_user import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    email = models.EmailField(unique=True, db_index=True)
    first_name = models.CharField(max_length=30, db_index=True)
    last_name = models.CharField(max_length=30, db_index=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_activity = models.DateTimeField(default=timezone.now)
    is_2fa_enabled = models.BooleanField(default=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='O', blank=True, null=True)
    objects = CustomUserManager()
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_avatar(self):
        if self.gender == "M":
            return static('images/male.jpeg')
        elif self.gender == "F":
            return static('images/female.jpeg')
        return static('images/default_avatar.png')

    def toggle_2fa(self):
        self.is_2fa_enabled = not self.is_2fa_enabled
        self.save()

    @property
    def is_online(self):
        last_active = cache.get(f'user_{self.pk}_last_activity')

        if last_active is None:
            last_active = self.last_activity

        if last_active is None:
            return False

        return timezone.now() - last_active < timedelta(minutes=5)

    @cached_property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'users_user'
        ordering = ['-created_at']

        indexes = [
            models.Index(fields=['first_name'], name='first_name_idx'),
            models.Index(fields=['last_name'], name='last_name_idx'),
            models.Index(fields=['first_name', 'last_name'], name='first_last_name_idx'),
        ]

    def switch_activity(self):
        self.is_active = not self.is_active
        self.save()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
