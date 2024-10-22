from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('chart-data/', views.get_chart_data, name='chart_data'),
    path('submit-data/', views.submit_data, name='submit_data'),
]
