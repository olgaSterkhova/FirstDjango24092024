from django.conf.urls import url

from . import views

app_name = 'Firstdjango'

urlpatterns = [
    url('', views.home, name='home'),
]