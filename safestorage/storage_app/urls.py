from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home, name='storage-home'),
    path('register/', views.register, name='storage-register'),
    path('login/', views.login, name='storage-login'),
    path('logout/', views.logout, name='storage-logout'),
    path('file_upload/', views.file_upload_page, name='storage-file_upload'),
    path('image_upload/', views.upload_auth_image, name='upload_auth_image'),

]
