from django.shortcuts import render
from .models import Visit

# Create your views here.
def home(request):
    post=Visit.objects.all()
    return render(request,'index.html',{'post':post})
