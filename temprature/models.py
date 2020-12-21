from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Sensor(models.Model):
    sensor_no = models.IntegerField()
    temp  = models.DecimalField( max_digits=5, decimal_places=2)
    humidity = models.DecimalField( max_digits=5, decimal_places=2)
    date  = models.DateTimeField()
    remark = models.TextField()

    def __str__(self):
        return self.remark

""" 
Temp	Humidity	Date	Remark
24.81	57.80%	18/12/2020 13:54	


 """        