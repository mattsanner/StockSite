from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from allauth.account import urls

# Create your views here.
def home(request):
    if(request.user.is_authenticated):
        return HttpResponse("Signed in Dashboard page woo!")
    else:
        return redirect(reverse('account_login'))