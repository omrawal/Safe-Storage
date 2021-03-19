from django.forms.widgets import HiddenInput
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User_data, Encrypted_files
from .file_crypto import *
from .forms import *

# Create your views here.


def home(request):
    return render(request, 'storage_app/home.html',)


# def register(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         four_digit_pass = request.POST.get('password')
#         private_key = generateKey()
#         profile_pic = request.FILES.get('profile_pic')
#         print(username)
#         print(email)
#         print(four_digit_pass)
#         print(private_key)
#         print(profile_pic)
#         print(type(profile_pic))

#     return render(request, 'storage_app/register.html',)


def register(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('storage-home')
    else:
        form = RegistrationForm(
            initial={'private_key': generateKey()})
    return render(request, 'storage_app/register.html', {'form': form})
