from django.urls import path
from . import views 
from .views import CustomLoginView
from .views import (
    StartupListView, StartupDetailView,
    CampaignListView, CampaignDetailView,
    DonationListView, DonationDetailView
)


app_name = 'campaigns'

urlpatterns = [
    path('', views.homepage, name='homepage'),
	path('register/', views.register, name='register'),
    path('admin-view/', views.admin_view, name='admin_view'),
    path('user-view/', views.user_view, name='user_view'),
	path('login/', CustomLoginView.as_view(), name='login'),
	path('startups/', StartupListView.as_view(), name='startup_list'),
    path('startups/<int:pk>/', StartupDetailView.as_view(), name='startup_detail'),
    path('campaigns/', CampaignListView.as_view(), name='campaign_list'),
    path('campaigns/<int:pk>/', CampaignDetailView.as_view(), name='campaign_detail'),
    path('donations/', DonationListView.as_view(), name='donation_list'),
    path('donations/<int:pk>/', DonationDetailView.as_view(), name='donation_detail'),
]