import factory
from campaigns.models import Startup, Campaign, Donation
from faker import Faker
from datetime import timedelta
import random

faker = Faker()

class StartupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Startup

    name = factory.Faker('company')
    description = factory.Faker('text', max_nb_chars=200)
    founders = factory.LazyAttribute(lambda _: f"{faker.name()}, {faker.name()}")
    established_date = factory.Faker('date_between', start_date='-10y', end_date='-1y')

class CampaignFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Campaign

    name = factory.Faker('catch_phrase')
    description = factory.Faker('text', max_nb_chars=300)
    goal_amount = factory.LazyAttribute(lambda _: random.randint(1000, 10000))
    collected_amount = factory.LazyAttribute(lambda _: random.randint(0, 5000))
    start_date = factory.Faker('date_between', start_date='-1y', end_date='today')
    end_date = factory.Faker('date_between', start_date='today', end_date='+1y')
    startup = factory.SubFactory(StartupFactory)

class DonationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Donation

    user_name = factory.Faker('name')
    campaign = factory.SubFactory(CampaignFactory)
    amount = factory.LazyAttribute(lambda _: random.randint(10, 1000))
    donation_date = factory.Faker('date_between', start_date='-1y', end_date='today')
