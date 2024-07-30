from django.db import models
from users.models import Author
from django.contrib.auth.models import AbstractUser
from users.validators import validate_password_strength, validate_email

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

    class Meta:
        abstract = False

    def __str__(self):
        return self.email


class Subscription(models.Model):
    subscriber = models.ForeignKey(
        Subscribed,
        on_delete=models.CASCADE,
        related_name='subscriptions',
        verbose_name='subscriber'
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='subscriptions',
        verbose_name='author'
    )
    subscribed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('subscriber', 'author')
        verbose_name = 'subscription'
        verbose_name_plural = 'subscriptions'

    def __str__(self):
        return f'{self.subscriber} -> {self.author}'