from django.urls import path
from . import views

urlpatterns = [
    path('',views.log_in),
    path('sign_up',views.sign_up),
    path('log_in',views.relogin),
    path('signup',views.signup),
    path('home',views.home),
    path('login',views.login),
    path('log_out',views.log_out)
]
