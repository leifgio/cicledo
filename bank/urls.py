from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('sms/', views.index, name='sms'),
    path('payment/', views.payment , name='payment'),
    path('changePassword/', views.changePassword, name='changePassword'),
    path('loginDebtor/', views.loginDebtor, name='loginDebtor'),
]

