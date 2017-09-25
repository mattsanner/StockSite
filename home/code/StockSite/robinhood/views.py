from django.shortcuts import render, redirect
from django.urls import reverse
from django.template import loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_protect

from . import forms
from .services import RobinhoodServices



# Create your views here.
#not really a view, probably needs to be moved
"""
@csrf_protect
def register(request, username, password):
    if(request.user.is_authenticated and request.method == 'POST'):
        try:
            print("wtf is going on here")
            RobinhoodServices.authenticate(request.user, username, password) 
            template = loader.get_template("robinhood/success.html")
            print("About to return response")            
            return HttpResponseRedirect(template.render())
        except:
            return redirect(reverse('registration_error'))
    else:
        return redirect(reverse('registration_error'))

@csrf_protect
def registration(request):
    if request.user.is_authenticated:
        try:
            request.user.robinhooduser
        except (ObjectDoesNotExist):
            template = loader.get_template("robinhood/registration.html")
            return HttpResponse(template.render())
    else:
        return redirect(reverse('account_login'))
    """
def registration(request):
    if(request.user.is_authenticated and request.method == 'POST'):
        form = forms.RobinhoodRegistrationForm(request.POST)
        if(form.is_valid()):
            try:
                RobinhoodServices.register(request.user, form.cleaned_data['username'], form.cleaned_data['password'])
                template = loader.get_template("robinhood/success.html")
                return HTTPResponseRedirect(template.Render())
            except Exception as e:
                return render(request, 'robinhood/registration_error.html', {'error_message': e})
    else:
        form = forms.RobinhoodRegistrationForm()
    
    return render(request, 'robinhood/registration.html', {'form': form})

def robinhoodsignin(request):
    if request.user.is_authenticated:
        template = loader.get_template("robinhood/signin.html")
        return HttpResponse(template.render())
    else:
        return redirect(reverse('account_login'))