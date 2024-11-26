from django.db import models

# Create your models here.
class Startup(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    founders = models.CharField(max_length=200)
    established_date = models.DateField()

    def __str__(self):
        return self.name

class Campaign(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    goal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    collected_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    start_date = models.DateField()
    end_date = models.DateField()
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Donation(models.Model):
    user_name = models.CharField(max_length=100)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    donation_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name} - {self.amount} to {self.campaign.name}"