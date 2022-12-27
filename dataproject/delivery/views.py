from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required



# Create your views here.
def home(request):
    return render(request,"delivery/home.html")

@login_required(login_url='../accounts/login/')
def status(request):
    return render(request,"delivery/status.html")

@permission_required("delivery.view_staff",login_url='../accounts/login/')
def address(request):
    return render(request,"delivery/address.html")