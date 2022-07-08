from django.shortcuts import render, redirect
from .models import Debtor, Loan, Payment
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views import generic

from bank.forms import *

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

def generatePdf(request,pk):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch,inch)
    textob.setFont("Helvetica",14)

    payment = Payment.objects.all()

    lines = []

    for x in payment:
        lines.append(x.debtor_id)


    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    
    return FileResponse(buf, as_attachment=True, filename='receipt.pdf')

@login_required(login_url='bank:login')
def sms(request):
    return render(request, "sms.html")

def debtor(request):
    return render(request, "debtors.html")

@login_required(login_url='bank:login')
def dashboard(request):
    debtor = Debtor.objects.all()
    queries = {'debtor': debtor}
    return render(request, "dashboard.html", queries)

@login_required(login_url='bank:login')
def createDebtor(request):
    form = CreateDebtor()
    if request.method == 'POST':
        debtor = CreateDebtor(request.POST)
        if debtor.is_valid():
            debtor.save()
            return redirect('bank:dashboard')
    value = {'form':form}
    return render(request, 'create.html',value)

@login_required(login_url='bank:login')
def updateDebtor(request,pk):
    updateditem = Debtor.objects.get(id=pk)
    form = CreateDebtor(instance=updateditem)
    if request.method == "POST":
        debtor = CreateDebtor(request.POST,instance=updateditem)
        if debtor.is_valid:
            debtor.save()
            return redirect('bank:dashboard')

    value = {'form':form}
    return render(request, 'create.html',value)

@login_required(login_url='bank:login')
def updateLoan(request,pk):
    updateditem = Loan.objects.get(id=pk)
    form = CreateLoan(instance=updateditem)
    if request.method == "POST":
        loan = CreateLoan(request.POST,instance=updateditem)
        if loan.is_valid:
            loan.save()
            return redirect('bank:dashboard')

    value = {'form':form}
    return render(request, 'create.html',value)

@login_required(login_url='bank:login')
def deleteDebtor(request,pk):
    deleteitem = Debtor.objects.get(id=pk)
    if request.method == "POST":
        deleteitem.delete()
        return redirect('bank:dashboard')
    value = {'item':deleteitem}
    return render(request, 'create.html',value)

@login_required(login_url='bank:login')
def deleteLoan(request,pk):
    deleteitem = Loan.objects.get(id=pk)
    if request.method == "POST":
        deleteitem.delete()
        return redirect('bank:dashboard')
    value = {'item':deleteitem}
    return render(request, 'create.html',value)

@login_required(login_url='bank:login')
def createLoan(request):
    form = CreateLoan()
    if request.method == 'POST':
        loan = CreateLoan(request.POST)
        if loan.is_valid():
            loan.save()
    value = {'form':form}
    return render(request, 'create.html',value)

class DebtorDetail(generic.DetailView):
    model = Debtor
    template_name = 'debtors-detail.html'

@login_required(login_url='bank:login')
def createPayment(request):
    form = CreatePayment()
    if request.method == 'POST':
        payment = CreatePayment(request.POST)
        if payment.is_valid():
            payment.save()
            return redirect('bank:dashboard')
    value = {'form':form}
    return render(request, 'create.html',value)

def loginPage(request):
    if request.method == 'POST':
        un = request.POST.get('username')
        pw = request.POST.get('Password')

        user = authenticate(request, username = un, password =pw)

        if user is not None:
            login(request, user)
            return redirect('bank:dashboard')
    return render(request, "login.html")

def logoutPage(request):
    logout(request)
    return redirect('bank:login')

