from django.db import models
import requests

from .models import RobinhoodUser

class RobinhoodServices():

    def authenticate(user, username, password):
        if(user.robinhooduser == username):
            r = requests.post('https://api.robinhood.com/api-token-auth/', {"username": username, "password": password})
            data = r.json()
            if 'token' in data.keys():
                user = RobinhoodUser.objects.filter(username=username)            
                user.token = data['token']
            else:
                raise NotImplementedError()   #TODO log an error and possibly an error code/value in this case
        else:            
            raise NotImplementedError()   #TODO log an error and possibly return error code/value in this case

    def register(user, username, password):           
        if user.robinhooduser.exists or user.robinhooduser != username:
            return False
        user.robinhooduser.username = username
        user.save()
        RobinhoodServices.authenticate(user, username, password)   
        
    def get_stocks(username):
        r = requests