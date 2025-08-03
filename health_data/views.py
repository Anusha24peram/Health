from django.shortcuts import render
from .models import HealthRecord

def index(request):
    records = HealthRecord.objects.all()
    return render(request, 'health_data/index.html', {'records': records})
