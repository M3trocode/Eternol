import pandas as pd
from django.http import JsonResponse
from .models import PressureData
import csv
import io
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')
def submit_data(request):
    if request.method == 'POST':
        response_data = {}
        
        # Handle pasted data
        if 'data' in request.POST:
            pasted_data = request.POST['data']
            data_lines = pasted_data.strip().split('\n')
            for line in data_lines:
                try:
                    substance, min_pressure, depth_range, pressure_gradient = line.split(',')
                    PressureData.objects.create(
                        substance=substance.strip(),
                        min_pressure=float(min_pressure.strip()),
                        depth_range=float(depth_range.strip()),
                        pressure_gradient=float(pressure_gradient.strip())
                    )
                except ValueError:
                    continue

        # Handle uploaded CSV data
        elif request.FILES.get('csv_file'):
            csv_file = request.FILES['csv_file']
            if csv_file.name.endswith('.csv'):
                decoded_file = csv_file.read().decode('utf-8')
                io_string = io.StringIO(decoded_file)
                next(io_string)  # Skip the header if present
                for line in io_string:
                    try:
                        substance, min_pressure, depth_range, pressure_gradient = line.split(',')
                        PressureData.objects.create(
                            substance=substance.strip(),
                            min_pressure=float(min_pressure.strip()),
                            depth_range=float(depth_range.strip()),
                            pressure_gradient=float(pressure_gradient.strip())
                        )
                    except ValueError:
                        continue

        # Return updated graph data
        pressure_data = list(PressureData.objects.all().values('substance', 'min_pressure', 'depth_range'))
        response_data['graph_data'] = pressure_data
        return JsonResponse(response_data)

    return JsonResponse({'error': 'Invalid request'}, status=400)

def get_graph_data(request):
    # Fetch data for the graph
    pressure_data = list(PressureData.objects.all().values('substance', 'min_pressure', 'depth_range'))
    return JsonResponse({'graph_data': pressure_data})
