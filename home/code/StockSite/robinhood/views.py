from django.shortcuts import render, redirect
from django.urls import reverse
from django.template import loader
from django.http import HttpResponse, HttpRequest
from django.core.exceptions import ObjectDoesNotExist

from . import models
from .services import RobinhoodServices



# Create your views here.
#not really a view, probably needs to be moved
def register(request, username, password):
    if(request.user.is_authenticated and request.method == 'POST'):
        try:
            RobinhoodServices.authenticate(request.user, username, password) 
            template = loader.get_template("robinhood/success.html")
            return HttpResponse(render(request, template))
        except:
            return redirect(reverse('registration_error'))
    else:
        return redirect(reverse('registration_error'))

def registration(request):
    if request.user.is_authenticated:
        try:
            request.user.robinhooduser
        except (ObjectDoesNotExist):
            template = loader.get_template("robinhood/registration.html")
            return HttpResponse(template.render())
    else:
        return redirect(reverse('account_login'))

def robinhoodsignin(request):
    if request.user.is_authenticated:
        template = loader.get_template("robinhood/signin.html")
        return HttpResponse(template.render())
    else:
        return redirect(reverse('account_login'))
