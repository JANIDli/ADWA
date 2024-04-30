from django.forms import ModelForm
from .models import BlogPost


class BlogForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'description', 'image']