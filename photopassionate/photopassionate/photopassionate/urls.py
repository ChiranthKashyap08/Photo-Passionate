"""photopassionate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from project import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.main_home, name='main_home'),
    path('main_home',views.main_home, name='main_home'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('home',views.home, name='home'),
    path('camera',views.camera, name='camera'),
    path('catagories',views.catagories, name='catagories'),
    path('lens',views.lens, name='lens'),
    path('gallery',views.gallery, name='gallery'),
    path('admin_home',views.admin_home, name='admin_home'),
    path('admin_camera',views.admin_camera, name='admin_camera'),
    path('admin_lens',views.admin_lens, name='admin_lens'),
    path('camera_display',views.camera_display, name='camera_display'),
    path('lens_bookings',views.lens_bookings, name='lens_bookings'),
    path('lens_display',views.lens_display, name='lens_display'),
    path('camera_bookings',views.camera_bookings, name='camera_bookings'),
    path('admin_login',views.admin_login, name='admin_login'),
    path('logout_u',views.logout_u, name='logout_u'),
    path('logout_a',views.logout_a, name='logout_a'),   
    path('deletec/<int:id>',views.deletec, name='deletec'),
    path('deletel/<int:id>',views.deletel, name='deletel'),

]
