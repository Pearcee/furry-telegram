from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Sensor(models.Model):
    sensor_no   = models.IntegerField()
    temp        = models.DecimalField( max_digits=5, decimal_places=2)
    humidity    = models.DecimalField( max_digits=5, decimal_places=2)
    date        = models.DateTimeField()
    remark      = models.TextField()

    def __str__(self):
        return self.remark

class Speedtest(models.Model):
    server_id   = models.IntegerField()	
    sponsor	    = models.CharField(max_length=32)
    servername	= models.CharField(max_length=32)
    timestamp   = models.DateTimeField()
    distance    = models.DecimalField( max_digits=16, decimal_places=4)
    ping	    = models.DecimalField( max_digits=16, decimal_places=4)
    download    = models.DecimalField( max_digits=16, decimal_places=4)
    upload	    = models.DecimalField( max_digits=16, decimal_places=4)
    share		= models.CharField(max_length=8)
    ipaddress 	= models.CharField(max_length=16)

    def __str__(self):
        return self.servername

class Online(models.Model):
    timestamp   = models.DateTimeField()
    ipaddress 	= models.CharField(max_length=16)
    name	    = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class Devices(models.Model):
    ipaddress 	= models.CharField(max_length=16)
    name	    = models.CharField(max_length=16)
    workgroup   = models.CharField(max_length=16)
    make        = models.CharField(max_length=16)
    mac         = models.CharField(max_length=16)
    model       = models.CharField(max_length=16)
    name        = models.CharField(max_length=16)

    def __str__(self):
        return self.name

""" 
Temp	Humidity	Date	Remark
24.81	57.80%	18/12/2020 13:54	

Server ID	Sponsor	Server Name	Timestamp	Distance	Ping	Download	Upload	Share	                IP Address
23968	Vodafone UK	Manchester	2020-11-09T21:05:38.547069Z	180.3072225	29.748	59335347.83	18323263.1		86.180.102.2

01/12/2020 00:00	 192.168.1.101	 p101
01/12/2020 00:00	 192.168.1.103	 p103

ip	Name	  Remark	WORKGROUP	Make	Mac	Model 	Column1
192.168.1.014	tv-sumsung			Samsung Electronics Co.,Ltd	5C:49:7D:D0:90:09		

 """        