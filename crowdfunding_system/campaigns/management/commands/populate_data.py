from django.core.management.base import BaseCommand
from campaigns.factories import StartupFactory, CampaignFactory, DonationFactory

class Command(BaseCommand):
    help = "Populate database with sample data for testing"

    def handle(self, *args, **kwargs):
        # Generiraj 5 startupa
        startups = [StartupFactory() for _ in range(5)]

        # Generiraj 10 kampanja
        campaigns = [CampaignFactory() for _ in range(10)]

        # Generiraj 15 donacija
        donations = [DonationFactory() for _ in range(15)]

        self.stdout.write(self.style.SUCCESS("Sample data successfully populated!"))
