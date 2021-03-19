from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=256, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    four_digit_pass = models.CharField(max_length=256, null=True, blank=True)
    private_key = models.CharField(max_length=256, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='static/profilepic')
