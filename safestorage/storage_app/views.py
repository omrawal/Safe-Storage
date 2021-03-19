from django.shortcuts import render
from .models import User_data, Encrypted_files
from .file_crypto import *

# Create your views here.


def home(request):
    return render(request, 'storage_app/home.html',)


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        four_digit_pass = request.POST.get('password')
        private_key = generateKey()
        print(username)
        print(email)
        print(four_digit_pass)
        print(private_key)

    return render(request, 'storage_app/register.html',)
