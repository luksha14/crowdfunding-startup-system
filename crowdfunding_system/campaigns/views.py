from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import Startup, Campaign, Donation
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