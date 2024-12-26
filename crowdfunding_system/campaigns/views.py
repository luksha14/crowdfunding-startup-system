from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import Startup, Campaign, Donation
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import StartupForm, CampaignForm, DonationForm
from django.http import HttpResponse

## Create your views here.
def homepage(request):
    if request.user.is_authenticated:
        return redirect('campaigns:user_view')  
    return render(request, 'base.html')
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, '/registration/register.html', {'form': form})

def is_admin(user):
    return user.is_superuser

class CustomLoginView(LoginView):
    def get_success_url(self):
        if self.request.user.is_superuser:
            return reverse_lazy('admin:index')  
        return reverse_lazy('campaigns:user_view')

@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')

@login_required
def user_view(request):
    startups = Startup.objects.all()
    campaigns = Campaign.objects.all()
    donations = Donation.objects.all()

    return render(request, 'user_view.html', {
        'startups': startups,
        'campaigns': campaigns,
        'donations': donations
    })

class StartupListView(ListView):
    model = Startup
    template_name = 'startup_list.html'
    context_object_name = 'startups'

    def get_queryset(self):
        query = self.request.GET.get('q')  
        if query:
            return Startup.objects.filter(
                Q(name__icontains=query) | Q(founders__icontains=query)
            )
        return Startup.objects.all()

class StartupDetailView(DetailView):
    model = Startup
    template_name = 'startup_detail.html'
    context_object_name = 'startup'

class CampaignListView(ListView):
    model = Campaign
    template_name = 'campaign_list.html'
    context_object_name = 'campaigns'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Campaign.objects.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            )
        return Campaign.objects.all()

class CampaignDetailView(DetailView):
    model = Campaign
    template_name = 'campaign_detail.html'
    context_object_name = 'campaign'

class DonationListView(ListView):
    model = Donation
    template_name = 'donation_list.html'
    context_object_name = 'donations'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Donation.objects.filter(
                Q(user_name__icontains=query) | Q(campaign__name__icontains=query)
            )
        return Donation.objects.all()

class DonationDetailView(DetailView):
    model = Donation
    template_name = 'donation_detail.html'
    context_object_name = 'donation'
    
class StartupCreateView(CreateView):
    model = Startup
    form_class = StartupForm
    template_name = 'startup_form.html'
    success_url = reverse_lazy('campaigns:startup_list')

class StartupUpdateView(UpdateView):
    model = Startup
    form_class = StartupForm
    template_name = 'startup_form.html'
    success_url = reverse_lazy('campaigns:startup_list')

class StartupDeleteView(DeleteView):
    model = Startup
    template_name = 'startup_confirm_delete.html'
    success_url = reverse_lazy('campaigns:startup_list')

class CampaignCreateView(CreateView):
    model = Campaign
    form_class = CampaignForm
    template_name = 'campaign_form.html'
    success_url = reverse_lazy('campaigns:campaign_list')

class CampaignUpdateView(UpdateView):
    model = Campaign
    form_class = CampaignForm
    template_name = 'campaign_form.html'
    success_url = reverse_lazy('campaigns:campaign_list')

class CampaignDeleteView(DeleteView):
    model = Campaign
    template_name = 'campaign_confirm_delete.html'
    success_url = reverse_lazy('campaigns:campaign_list')

class DonationCreateView(CreateView):
    model = Donation
    form_class = DonationForm
    template_name = 'donation_form.html'
    success_url = reverse_lazy('campaigns:donation_list')

class DonationUpdateView(UpdateView):
    model = Donation
    form_class = DonationForm
    template_name = 'donation_form.html'
    success_url = reverse_lazy('campaigns:donation_list')

class DonationDeleteView(DeleteView):
    model = Donation
    template_name = 'donation_confirm_delete.html'
    success_url = reverse_lazy('campaigns:donation_list')