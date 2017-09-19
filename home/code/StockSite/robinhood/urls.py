from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^signin', views.robinhoodsignin),
    url(r'^registration', views.registration),
    url(r'^register', views.register)
]