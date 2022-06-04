from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Debtor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=120)
    contact = PhoneNumberField(null=False,blank=False,unique=True)
    address = models.CharField(max_length=120)

    def __str__(self):
        return '%s-%s' % (self.pk, self.first_name)


class Loan(models.Model):
    LOAN_TYPES = (
        ('12 months to pay', '12 months to pay'),
        ('24 months to pay', '24 months to pay'),
        )
    STATUS_TYPES = (
        ('P', 'Paid'),
        ('U', 'Unpaid'),
        )
    debtor = models.ForeignKey(Debtor, on_delete=models.CASCADE)
    loan_type = models.CharField(max_length=24,choices=LOAN_TYPES)
    amount = models.IntegerField()
    payment_status =  models.CharField(max_length=2, choices=STATUS_TYPES)
    date_created = models.DateField()

    def __str__(self):
        return '%s,%s' % (self.loan_type, self.debtor)

class Payment(models.Model):
    loan_id = models.ForeignKey(Loan, on_delete=models.CASCADE)
    month = models.DateField()
    amount = models.IntegerField()

    def __str__(self):
        return '%s %s' % (self.month, self.loan_id)
