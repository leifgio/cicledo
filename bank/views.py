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

def loginDebtor(request):
    return render(request, "login-debtor.html")

def loginEmployee(request):
    return render(request, "login-employee.html")
