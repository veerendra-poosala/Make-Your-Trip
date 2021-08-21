from django.shortcuts import render,redirect
from django.contrib import auth,messages
from django.contrib.auth.models import User
from django.urls import reverse
# Create your views here.


def register(request):
    return render(request,'register.html')


def signup(request):
    if request.method=='POST':
        if request.POST['password1']==request.POST['password2']:
            try:
                user=User.objects.get(first_name=request.POST['first_name'])
                messages.info(request,'Username already exists')
                return render(request,'register.html')
                
            except User.DoesNotExist:
                user=User.objects.create_user(username=request.POST['first_name'],password=request.POST['password2'],first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'])
                auth.login(request,user)
                return redirect(reverse('register'))
        else:
            messages.info(request,'password must match')
            return render(request,'register.html')
    else:
        return redirect(request,'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['first_name']
        password=request.POST['password2']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'invalid credenitials')
            return redirect(reverse(login))
    else:
        return render(request,'login.html')

        
def logout(request):
    auth.logout(request)
    return redirect("/")




   





