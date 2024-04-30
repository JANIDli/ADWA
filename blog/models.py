from django.db import models
from django.urls import reverse
# Create your models here.


class BlogPost(models.Model):
    VOTE_TYPE = (
        ("up","up vote"),
        ("down","down vote"),
    )
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(default="default.jpg", upload_to="blog/", null=True, blank=True)
    vote = models.CharField(choices=VOTE_TYPE, max_length=200)

    def __str__(self):
        return self.title
    
    
        

class BlogComment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(max_length=500, null=True, blank=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.email
    