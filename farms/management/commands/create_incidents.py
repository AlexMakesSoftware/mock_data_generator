from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
import random
from random import choice
from datetime import date, timedelta
from farms.models import Incident, Farm

class Command(BaseCommand):
    help = 'Create farm incidents'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Indicates the total number of farms to have incidents, randomly allocated.')        

    @staticmethod
    def _generate_random_date(start_date, end_date=None):
        if end_date is None:
            end_date = date.today()
        else:
            end_date = min(end_date, date.today())
        random_days = random.randint(0, (end_date - start_date).days)
        random_date = start_date + timedelta(days=random_days)
        return random_date


    def handle(self, *args, **kwargs):
       
        count = kwargs['count']
        farms = Farm.objects.all()
        status_choices = ['S', 'C', 'E']
        earliest_date = date(2010, 1, 1)

        for _ in range(count):
            farm = choice(farms)
            status = choice(status_choices)
            start_date = Command._generate_random_date(earliest_date, date.today() - timedelta(days=10))

            if status == 'E':
                # Set end_date for 'ended' incidents
                end_date = Command._generate_random_date(start_date)
            else:
                end_date = None

            incident = Incident.objects.create(
                incident_number=Incident.generate_unique_incident_number(),
                start_date=start_date,
                end_date=end_date,
                status=status,
                farm=farm
            )

            self.stdout.write(self.style.SUCCESS(f"Created incident #{incident.id}"))
