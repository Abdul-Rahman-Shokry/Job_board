from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.ForeignKey('City',related_name='user_city', on_delete=models.CASCADE, null=True, blank=True)
    # Google : 'django phone field'
    phone_number = models.CharField(max_length=15)
    image = models.ImageField(upload_to='profile/')

    def __str__(self):
        return str(self.user)


## create a new user --> create a new profile
## Google : 'django signals'
"""
Go to https://simpleisbetterthancomplex.com/tutorial/2016/07/28/how-to-create-django-signals.html
Navigate to profiles/signals.py and copy the code
"""
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# Not a DB best practice
class City(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.name)