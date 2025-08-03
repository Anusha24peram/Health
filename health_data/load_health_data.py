import csv
from django.core.management.base import BaseCommand
from health_data.models import HealthRecord

class Command(BaseCommand):
    help = 'Load health data from CSV'

    def handle(self, *args, **kwargs):
        with open('path/to/synthetic_health_lifestyle_dataset.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                HealthRecord.objects.create(
                    age=int(row['age']),
                    gender=row['gender'],
                    height=float(row['height']),
                    weight=float(row['weight']),
                    smoker=row['smoker'].lower() == 'true',
                    exercise_frequency=row['exercise_frequency'],
                    diet_quality=row['diet_quality'],
                    disease_risk=row['disease_risk']
                )
        self.stdout.write(self.style.SUCCESS('Data loaded successfully.'))
