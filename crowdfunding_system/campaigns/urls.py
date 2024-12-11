from django.urls import path
from . import views 
from .views import CustomLoginView


app_name = 'campaigns'

urlpatterns = [
    path('', views.homepage, name='homepage'),
	path('register/', views.register, name='register'),
    path('admin-view/', views.admin_view, name='admin_view'),
    path('user-view/', views.user_view, name='user_view'),
	path('login/', CustomLoginView.as_view(), name='login'),
]