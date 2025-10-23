from django.shortcuts import render,redirect

# Create your views here.

def login(request):
    return render(request,'accounts/login.html')

def register(request):
    return render(request,'accounts/register.html')

def logout(request):
    return redirect('home')

def dashboard(request):
    return render(request,'accounts/dashboard.html')

