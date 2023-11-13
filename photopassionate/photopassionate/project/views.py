from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *

# Create your views here.

def login(request):
    if request.method=="POST":
        user=request.POST["email"]
        pswd=request.POST["password"]
        log=user_login.objects.get(email=user,password=pswd)
        if log:
            request.session['email']=user
            request.session['userid']=log.id
            return redirect('home')
        else:
            return render(request,'login.html')

    return render(request,'login.html')

def register(request):
    if request.method=="POST":
        cam=user_login()
        cam.name=request.POST['name']
        cam.email=request.POST['email']
        cam.password=request.POST['password']
        cam.save()
    return render(request,'register.html')

def home(request):
    if 'email' in request.session:
        mail=request.session['email']
        userid=request.session['userid']
        return render(request,'home.html',{'username':mail})
    else:
        return render(request,'login.html')

    return render(request,'home.html')

def catagories(request):
    return render(request,'catagories.html')

def camera(request):
    add=add_cam.objects.all()
    return render(request,'camera.html',{'cam':add})   

def lens(request):
    ladd=add_lens.objects.all()
    return render(request,'lens.html',{'lens':ladd})

def gallery(request):
    return render(request,'gallery.html')

def admin_home(request):
    if 'email' in request.session:
        mail=request.session['email']
        userid=request.session['userid']
        return render(request,'admin_home.html',{'username':mail})
    else:
        return render(request,'admin_login.html')

    return render(request,'admin_home.html')

def admin_camera(request):
    if request.method=="POST":
        cam=add_cam()
        cam.brand=request.POST['brand']
        cam.cam_models=request.POST['cam_models']
        cam.formfactor=request.POST['formfactor']
        cam.resolution=request.POST['resolution']
        cam.price=request.POST['price']
        cam.opticalzoom=request.POST['opticalzoom']
        cam.save()
    return render(request,'admin_camera.html')

def admin_lens(request):
    if request.method=="POST":
        lens=add_lens()
        lens.brand=request.POST['brand']
        lens.lenstype=request.POST['lenstype']
        lens.mount=request.POST['mount']
        lens.maxflength=request.POST['maxflength']
        lens.minflength=request.POST['minflength']
        lens.price=request.POST['price']
        lens.save()
    return render(request,'admin_lens.html')

def camera_display(request):
    add=add_cam.objects.all()
    return render(request,'camera_display.html',{'cam':add})

def lens_bookings(request):
    return render(request,'lens_bookings.html')

def lens_display(request):
    ladd=add_lens.objects.all()
    return render(request,'lens_display.html',{'lens':ladd})

def camera_bookings(request):
    return render(request,'camera_bookings.html')

def main_home(request):
    return render(request,'main_home.html')

def admin_login(request):
    if request.method=="POST":
        user=request.POST["email"]
        pswd=request.POST["password"]
        log=admn_lgin.objects.get(email=user,password=pswd)
        if log:
            request.session['email']=user
            request.session['userid']=log.id
            return redirect('admin_home')
        else:
            return render(request,'admin_login.html')

    return render(request,'admin_login.html')
def logout_u(request):
    del request.session['email']
    del request.session['userid']
    return render(request,'home.html')

def logout_a(request):
    del request.session['email']
    del request.session['userid']
    return render(request,'admin_home.html')

def deletec(request,id):
    cam=add_cam.objects.get(id=id)
    cam.delete()
    return redirect("camera_display")

def deletel(request,id):
    cam=add_lens.objects.get(id=id)
    cam.delete()
    return redirect("lens_display")

