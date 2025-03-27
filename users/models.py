from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('user', 'User'),
        ('artist', 'Artist'),
        ('admin', 'Admin'),
    ]
    email = models.EmailField(unique=True)
    avatar= models.ImageField(upload_to='avatars/', null=True, blank=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        return self.last_name if self.last_name else self.username

class Artist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    social_links = models.JSONField(blank=True, null=True)
    backdrop_img= models.ImageField(upload_to='backdrop/', null=True, blank=True)
    def __str__(self):
        return self.user.last_name if self.user.last_name else self.user.username

class Follower(models.Model):
    follower = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    followed_at = models.DateTimeField(auto_now_add=True)
