from django.db import models

from django.db import models

class PressureData(models.Model):
    substance = models.CharField(max_length=20)  # Oil, Water, or Gas
    min_pressure = models.FloatField()
    depth_range = models.FloatField()
    pressure_gradient = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.substance} - {self.min_pressure} psia at {self.depth_range} ft"

