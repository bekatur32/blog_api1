from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_password_strength, validate_email


class Author(AbstractUser):
    email = models.EmailField(unique=True, validators=[validate_email])
    password = models.CharField("password", validators=[validate_password_strength], max_length=128)
    can_create_blogs = models.BooleanField(default=True)
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='author_user_permissions'  # Уникальный related_name
    )

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='author_groups'  # Уникальный related_name
    )

    def __str__(self):
        return self.email


class Subscribed(AbstractUser):
    email = models.EmailField(unique=True, validators=[validate_email])
    password = models.CharField("password", validators=[validate_password_strength], max_length=128)
    can_create_blogs = models.BooleanField(default=False)
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='subscribed_user_permissions'  # Уникальный related_name
    )

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='subscribed_groups'  # Уникальный related_name
    )

    def __str__(self):
        return self.email
