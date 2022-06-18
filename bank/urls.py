from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('sms/', views.sms, name='sms'),
    path('payment/', views.payment , name='payment'),
    path('debtors/', views.debtor, name='debtors'),
    path('dummy/', views.dummy, name='dummy'),
    path('<int:pk>/', views.dummy, name='user'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
]

