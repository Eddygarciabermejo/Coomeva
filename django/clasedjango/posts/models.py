from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    website= models.URLField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    picture = models.ImageField( upload_to='user/pictures', blank=True, null=True )
    created = models.DateTimeField( auto_now_add=True )
    modified = models.DateTimeField( auto_now=True )

    def __str__(self):
        return self.user.username