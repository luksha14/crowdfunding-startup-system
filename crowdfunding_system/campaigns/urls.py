from django.urls import path
from . import views

app_name = 'campaigns'

urlpatterns = [
    path('', views.homepage, name='homepage'),
]