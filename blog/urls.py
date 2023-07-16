from django.urls import path
from . import views

"""
URL config for 'blog' app

"""

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='homepage'),
]
