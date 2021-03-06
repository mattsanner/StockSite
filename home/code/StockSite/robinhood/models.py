from django.db import models
from django.conf import settings

# Create your models here.
class RobinhoodUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    token = ""
    
    def __str__(self):
        return self.username