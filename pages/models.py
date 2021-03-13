from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class contact(models.Model):
    Sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=150)
    textfield = models.TextField()

    def __str__(self):
        return 'Message From ' + self.name

class extUser(models.Model):
    phone = models.IntegerField(max_length=15)
    profileimg = models.ImageField(upload_to='profile/images',default='/profile/images/defaultp.jpg',max_length=500)
    age = models.IntegerField()
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return 'Profile of ' + self.user.first_name