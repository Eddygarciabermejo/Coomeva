from django.contrib.auth.models import User
from django.db import models

# Create your models here.

##class User(models.Model):
#    email = models.EmailField( unique=True )
#    password = models.CharField( max_length=100 )

 #   first_name= models.CharField( max_length=100 )
 #   last_name= models.CharField( max_length=100 )

#    is_admin = models.BooleanField( default=False )

#    bio = models.TextField()
#    birthdate = models.DateField( blank=True, null=True )
#   created = models.DateTimeField( auto_now_add=True )
#    modified = models.DateTimeField( auto_now=True )
#    

class Publicacion(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    profile = models.ForeignKey('posts.profile', on_delete=models.CASCADE)
    tittle = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='pots/photos')
    create = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} by @{}'.format(self.tittle, self.user.username)
