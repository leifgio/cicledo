from django.forms import ModelForm
from .models import *
from django import forms

class CreateDebtor(ModelForm):
    class Meta:
        model = Debtor
        fields = ['first_name', 'last_name', 'email', 'contact', 'address']

class CreateLoan(ModelForm):
    class Meta:
        model = Loan
        fields = ['debtor', 'loan_type', 'amount', 'payment_status']


class CreatePayment(ModelForm):
    class Meta:
        model = Payment
        fields = ['debtor_id', 'loan_id', 'month_number', 'amount']
