from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=256, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    four_digit_pass = models.CharField(max_length=256, null=True, blank=True)
    private_key = models.CharField(max_length=256, null=True, blank=True)
    auth_image = models.ImageField(
        upload_to='static/auth_image/%s' % username, null=True)
    profile_pic = models.ImageField(upload_to='static/profilepic', null=True)


class Encrypted_files(models.Model):
    owner = models.ForeignKey('User', null=True)
    encrypted_file = models.FileField(
        upload_to='static/encrypted_files', null=True)
    date_uploaded = models.DateTimeField(auto_now_add=True, null=True)
