from django.contrib import admin
from .models import *
# Register your models here.
model_list = [Startup, Donation, Campaign]
admin.site.register(model_list)