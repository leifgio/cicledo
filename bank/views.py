from django.shortcuts import render, redirect
from .models import Debtor, Loan, Payment
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from bank.forms import CreateDebtor,CreateLoan, CreatePayment

@login_required(login_url='login')
def sms(request):
    return render(request, "sms.html")

@login_required(login_url='login')
def payment(request):
    loan = Loan.objects.all()
    queries = {'loan': loan}
    return render(request, "payment.html", queries)

def debtor(request):
    return render(request, "debtors.html")

@login_required(login_url='login')
def dashboard(request):
    debtor = Debtor.objects.all()
    queries = {'debtor': debtor}
    return render(request, "dashboard.html", queries)

def dummy(request):
    debtor = Debtor.objects.all()
    loan = Loan.objects.all()
    payment = Payment.objects.all
    queries = {'debtor': debtor, 'loan': loan, 'payment':payment}
    return render(request, 'dummy.html', queries)

def loginPage(request):
    if request.method == 'POST':
        un = request.POST.get('username')
        pw = request.POST.get('Password')

        user = authenticate(request, username = un, password =pw)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, "login.html")

def logoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def createDebtor(request):
    form = CreateDebtor()
    if request.method == 'POST':
        debtor = CreateDebtor(request.POST)
        if debtor.is_valid():
            debtor.save()
    value = {'form':form}
    return render(request, 'create-debtor.html',value)

@login_required(login_url='login')
def createLoan(request):
    form = CreateLoan()
    if request.method == 'POST':
        loan = CreateLoan(request.POST)
        if loan.is_valid():
            loan.save()
    value = {'form':form}
    return render(request, 'create-debtor.html',value)

@login_required(login_url='login')
def createPayment(request):
    form = CreatePayment()
    if request.method == 'POST':
        payment = CreateLoan(request.POST)
        if payment.is_valid():
            payment.save()
    value = {'form':form}
    return render(request, 'create-payment.html',value)
