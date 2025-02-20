from django.urls import path
from . import views 
from .views import CustomLoginView
from .views import (
    StartupListView, StartupDetailView,
    CampaignListView, CampaignDetailView,
    DonationListView, DonationDetailView
)
from .views_api import (
    StartupListCreateView, StartupDetailView,
    CampaignListCreateView, CampaignDetailView,
    DonationListCreateView, DonationDetailView
)
from .views import *


app_name = 'campaigns'

urlpatterns = [
    path('', views.homepage, name='homepage'),
	path('register/', views.register, name='register'),
    path('admin-view/', views.admin_view, name='admin_view'),
    path('user-view/', views.user_view, name='user_view'),
	path('login/', CustomLoginView.as_view(), name='login'),
	
	path('startups/', StartupListView.as_view(), name='startup_list'),
    path('startups/<int:pk>/', StartupDetailView.as_view(), name='startup_detail'),
    path('startups/create/', StartupCreateView.as_view(), name='startup_create'),
    path('startups/<int:pk>/update/', StartupUpdateView.as_view(), name='startup_update'),
    path('startups/<int:pk>/delete/', StartupDeleteView.as_view(), name='startup_delete'),

    path('campaigns/', CampaignListView.as_view(), name='campaign_list'),
    path('campaigns/<int:pk>/', CampaignDetailView.as_view(), name='campaign_detail'),
    path('campaigns/create/', CampaignCreateView.as_view(), name='campaign_create'),
    path('campaigns/<int:pk>/update/', CampaignUpdateView.as_view(), name='campaign_update'),
    path('campaigns/<int:pk>/delete/', CampaignDeleteView.as_view(), name='campaign_delete'),

    path('donations/', DonationListView.as_view(), name='donation_list'),
    path('donations/<int:pk>/', DonationDetailView.as_view(), name='donation_detail'),
    path('donations/create/', DonationCreateView.as_view(), name='donation_create'),
    path('donations/<int:pk>/update/', DonationUpdateView.as_view(), name='donation_update'),
    path('donations/<int:pk>/delete/', DonationDeleteView.as_view(), name='donation_delete'),

	path('api/startups/', StartupListCreateView.as_view(), name='api_startup_list_create'),
    path('api/startups/<int:pk>/', StartupDetailView.as_view(), name='api_startup_detail'),
    path('api/campaigns/', CampaignListCreateView.as_view(), name='api_campaign_list_create'),
    path('api/campaigns/<int:pk>/', CampaignDetailView.as_view(), name='api_campaign_detail'),
    path('api/donations/', DonationListCreateView.as_view(), name='api_donation_list_create'),
    path('api/donations/<int:pk>/', DonationDetailView.as_view(), name='api_donation_detail'),
]