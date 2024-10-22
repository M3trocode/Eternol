from django.shortcuts import render
from .forms import DataInputForm
from .models import PressureData
import pandas as pd
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

def dashboard_view(request):
    if request.method == 'POST':
        form = DataInputForm(request.POST, request.FILES)
        if form.is_valid():
            if form.cleaned_data['csv_file']:
                # Handle CSV file
                csv_file = form.cleaned_data['csv_file']
                data = pd.read_csv(csv_file)
                # Process CSV data and save to model
            elif form.cleaned_data['data']:
                # Process pasted data
                raw_data = form.cleaned_data['data']
                # Parse raw data and save to mod
    else:
        form = DataInputForm()

    return render(request, 'index.html', {'form': form})

def get_chart_data(request):
    # Query data from the database
    gas_data = PressureData.objects.filter(substance="Gas")
    oil_data = PressureData.objects.filter(substance="Oil")
    water_data = PressureData.objects.filter(substance="Water")

    # Prepare data for Chart.js
    chart_data = {
        "gas": {"pressure": [d.min_pressure for d in gas_data], "depth": [d.depth_range for d in gas_data]},
        "oil": {"pressure": [d.min_pressure for d in oil_data], "depth": [d.depth_range for d in oil_data]},
        "water": {"pressure": [d.min_pressure for d in water_data], "depth": [d.depth_range for d in water_data]},
    }
    return JsonResponse(chart_data)



@api_view(['POST'])
def submit_data(request):
    # Your logic to handle the data submission
    return Response({'status': 'Data submitted successfully!'})
