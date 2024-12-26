from django import forms
from .models import Startup, Campaign, Donation

class StartupForm(forms.ModelForm):
    class Meta:
        model = Startup
        fields = ['name', 'description', 'founders', 'established_date']

class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ['name', 'description', 'goal_amount', 'start_date', 'end_date', 'startup']

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['user_name', 'campaign', 'amount']
