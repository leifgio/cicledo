from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.timezone import now

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
    loan_type = models.CharField(default="24 months to pay", max_length=24,choices=LOAN_TYPES)
    amount = models.IntegerField()
    payment_status =  models.CharField(default="U", max_length=2, choices=STATUS_TYPES)
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
