from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group

class InstaUser(AbstractUser):
    bio = models.TextField()
    link = models.URLField()
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        related_name='insta_users_permissions',
        related_query_name='insta_user_permissions',
    )
    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        related_name='insta_users_group',
        related_query_name='insta_user_group',
    )