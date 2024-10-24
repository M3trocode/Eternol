# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submit-data/', views.submit_data, name='submit_data'),
    path('get-graph-data/', views.get_graph_data, name='get_graph_data'),
]