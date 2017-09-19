from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.urls import reverse
from django.template import loader

# Create your views here.
def home(request):
    if(request.user.is_authenticated):
        template = loader.get_template('dashboard/index.html')                               
        return HttpResponse(template.render())
    else:
        return redirect(reverse('account_login'))