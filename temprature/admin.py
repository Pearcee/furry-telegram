from django.contrib import admin

# Register your models here.
from .models import Sensor, Speedtest, Online, Devices

admin.site.register(Sensor)
admin.site.register(Speedtest)
admin.site.register(Online)
admin.site.register(Devices)
