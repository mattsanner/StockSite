from django.shortcuts import render, redirect
from django.urls import reverse
from django.template import loader
from django.http import HttpResponse, HttpRequest
from django.core.exceptions import ObjectDoesNotExist
from . import models




# Create your views here.
#not really a view, probably needs to be moved
def register(request, username, password):
    if(request.user.is_authenticated):
        try:
            request.user.robinhooduser        
        except models.RobinhoodUser.DoesNotExist as e:
            request.user.token = robinhood.GetToken(username, password)
            return redirect(reverse('home'))
        except:
            return redirect(reverse('registration_error'))
    else:
        return null

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
