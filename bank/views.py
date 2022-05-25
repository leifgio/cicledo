from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "sms.html")

def dashboard(request):
    return render(request, "dashboard.html")

def payment(request):
    return render(request, "payment.html")

def changePassword(request):
    return render(request, "changepassword.html")

def debtor(request):
    return render(request, "debtors.html")

def login(request):
    return render(request, "login.html")
