from django.db.models.signals import post_delete, post_save
from django.contrib.auth.models import User
from .models import Profile


    
def create_user(sender,created,instance,**kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username
        )


def delete_user(sender, instance, **kwargs):
    user = instance.user
    user.delete()

post_save.connect(create_user, sender=User)
post_delete.connect(delete_user, sender=Profile)