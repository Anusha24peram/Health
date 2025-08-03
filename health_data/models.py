from django.db import models

class HealthRecord(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    height = models.FloatField()
    weight = models.FloatField()
    smoker = models.BooleanField()
    exercise_frequency = models.CharField(max_length=50)
    diet_quality = models.CharField(max_length=50)
    disease_risk = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.gender}, {self.age} yrs"
