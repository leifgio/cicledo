from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.timezone import now
import sys, requests, urllib

class Debtor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=120)
    contact = PhoneNumberField(null=False,blank=False,unique=True)
    address = models.CharField(max_length=120)

    def __str__(self):
        return '%s-%s' % (self.pk, self.first_name)

    def save(self, *args, **kwargs):
        apikey = '5b99abb653c56d436a0286df4b5020ad'
        number = f'{self.contact}'
        message = f'hi {self.first_name} you are now registered to CICLEDO loans'

        params = (
            ('apikey', apikey),
            ('message', message),
            ('number', number)
        )

        path = 'https://semaphore.co/api/v4/messages?' + urllib.parse.urlencode(params)

        requests.post(path)
        return super().save(*args, **kwargs)

class Loan(models.Model):
    LOAN_TYPES = (
        ('12 months to pay', '12 months to pay'),
        ('24 months to pay', '24 months to pay'),
        )
    STATUS_TYPES = (
        ('Paid', 'Paid'),
        ('Unpaid', 'Unpaid'),
        )
    debtor = models.ForeignKey(Debtor, on_delete=models.CASCADE)
    loan_type = models.CharField(default="24 months to pay", max_length=24,choices=LOAN_TYPES)
    amount = models.PositiveIntegerField()
    payment_status =  models.CharField(default="Unpaid", max_length=24, choices=STATUS_TYPES)
    date_created = models.DateField(default=now, editable=False)

    def __str__(self):
        return '%s,%s' % (self.loan_type, self.debtor)

class Payment(models.Model):
    debtor_id = models.ForeignKey(Debtor, on_delete=models.CASCADE)
    loan_id = models.ForeignKey(Loan, on_delete=models.CASCADE)
    month_number= models.IntegerField()
    amount = models.IntegerField()

    def __str__(self):
        return '%s %s' % (self.month_number, self.loan_id)

    def sum_payments(self):
        pass

