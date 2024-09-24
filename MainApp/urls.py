from django.conf.urls import url

from . import views

app_name = 'Firstdjanga'

urlpatterns = [
    url('', views.home, name='home'),
]