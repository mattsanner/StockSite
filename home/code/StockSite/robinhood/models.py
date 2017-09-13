from django.db import models
from django.conf import settings
import requests

# Create your models here.
class RobinhoodUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    token = ""
    
    def __str__(self):
        return self.username

class Robinhood(models.Model):

    def GetToken(username, password):
        r = requests.post('https://api.robinhood.com/api-token-auth/', {"username": username, "password": password})
        return r.token