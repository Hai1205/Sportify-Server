from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
import uuid

class User(AbstractUser):
    USER_ROLE_CHOICES = [
        ('user', 'User'),
        ('artist', 'Artist'),
        ('admin', 'Admin'),
    ]
    
    USER_STATUS = [
        ('pending', 'Pending'),
        ('locked', 'Locked'),
        ('active', 'Active'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(unique=True, max_length=10, null=False, blank=False)
    email = models.EmailField(unique=True, max_length=255, null=False, blank=False)
    password = models.CharField(max_length=255, null=False, blank=False)
    fullName = models.CharField(max_length=255, null=False, blank=False, default='fullName')
    avatarUrl = models.URLField(default='avatar.com')
    role = models.CharField(max_length=10, choices=USER_ROLE_CHOICES, default='user')
    status = models.CharField(max_length=10, choices=USER_STATUS, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Override lại quan hệ groups và permissions
    # groups = models.ManyToManyField(Group)
    # user_permissions = models.ManyToManyField(Permission)

    class Meta:
        db_table = "users"

    def __str__(self):
        return f"{self.id} ({self.role})"
