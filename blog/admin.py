from django.contrib import admin
from .models import BlogComment, BlogPost


admin.site.register(BlogComment)
admin.site.register(BlogPost)

# Register your models here.
