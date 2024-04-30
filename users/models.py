from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to="profiles", null=True, blank=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username

    
