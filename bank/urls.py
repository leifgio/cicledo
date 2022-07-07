from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'bank'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('sms/', views.sms, name='sms'),
    path('payment/', views.createPayment , name='payment'),
    path('debtors/', views.debtor, name='debtors'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),

    path('createDebtor/', views.createDebtor, name='create-debtor'),
    path('createLoan/', views.createLoan, name='create-loan'),

    path('update-debtor/<str:pk>/', views.updateDebtor, name='update-debtor'),
    path('delete-debtor/<str:pk>/', views.deleteDebtor, name='delete-debtor'),

    path('update-loan/<str:pk>/', views.updateLoan, name='update-loan'),
    path('delete-loan/<str:pk>/', views.deleteLoan, name='delete-loan'),

    path('<int:pk>/', login_required(views.DebtorDetail.as_view()), name='debtor-detail'),
    
    path('pdf-print/<str:pk>/', views.generatePdf, name='pdf-print'),
]


