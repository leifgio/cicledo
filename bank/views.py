from django.shortcuts import render
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, "sms.html")

def login(request):
    return render(request, "login.html")

def payment(request):
    return render(request, "payment.html")

def changePassword(request):
    return render(request, "changepassword.html")

def debtor(request):
    return render(request, "debtors.html")

def dashboard(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, "payment.html") 
    else:
        return render(request, "sms.html") 
