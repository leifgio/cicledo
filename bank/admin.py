from django.contrib import admin

from .models import Debtor, Loan, Payment

admin.site.register(Debtor)
admin.site.register(Loan)
admin.site.register(Payment)
