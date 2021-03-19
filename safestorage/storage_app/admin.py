from django.contrib import admin
from .models import User_data, Encrypted_files
# Register your models here.
admin.site.register(User_data)
admin.site.register(Encrypted_files)
# admin.site.register(auth_Image)
