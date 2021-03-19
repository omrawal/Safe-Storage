from django.forms.widgets import HiddenInput
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User_data, Encrypted_files
from .file_crypto import *
from .forms import *

# Create your views here.

is_authenticated = False
authenticate_user_obj = None
# print(type(list(User_data.objects.filter(username='om_rawal'))))
# print(list(User_data.objects.filter(username='om_rawal')))


def home(request):
    return render(request, 'storage_app/home.html',)


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


def upload_auth_image(request):
    return render(request, 'storage_app/upload_auth_image.html',)


def file_upload_page(request):
    global authenticate_user_obj
    global is_authenticated
    if(is_authenticated == False or authenticate_user_obj == None):
        return redirect('storage-login')
    all_files_list = list(Encrypted_files.objects.all())
    user_file_objects = []
    for i in all_files_list:
        if i.owner.username == authenticate_user_obj.username:
            user_file_objects.append(i)

    return render(request, 'storage_app/file_upload.html', {'user_obj': authenticate_user_obj, 'files': user_file_objects})


def logout(request):
    global is_authenticated
    global authenticate_user_obj
    is_authenticated = False
    authenticate_user_obj = None
    return redirect('storage-login')


def login(request):
    global is_authenticated
    global authenticate_user_obj
    if request.method == 'POST':
        enterd_uname = request.POST.get('username')
        entered_pass = request.POST.get('password')
        print(User_data.objects.all())
        user_data_lst = list(User_data.objects.filter(username=enterd_uname))
        # print(user_data)
        if(len(user_data_lst) == 1):
            user_data = user_data_lst[0]
            if(user_data.four_digit_pass == entered_pass):
                is_authenticated = True
                authenticate_user_obj = user_data
        # print(enterd_uname)
        # print(entered_pass)
        return redirect('storage-file_upload')
    else:
        form = RegistrationForm(
            initial={'private_key': generateKey()})
    # return render(request, 'storage_app/register.html', {'form': form})
    return render(request, 'storage_app/login.html',)
