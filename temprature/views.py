from django.shortcuts import render
from django.core import serializers
from . models import Sensor, Devices, Online, Speedtest
import json

from django.http import HttpResponse
from django.views.decorators.http import require_GET


# Create your views here.
def index(request):
	template='temprature/index.html'
	results=Sensor.objects.all()
	context={
		'results':results,
	}
	return render(request,template,context)

def devices(request):
	template='temprature/devices.html'
	results=Devices.objects.all()
	context={
		'results':results,
	}
	return render(request,template,context)


def sensor(request):
	template='temprature/sensor.html'
	results=Sensor.objects.all()
	context={
		'results':results,
	}
	return render(request,template,context)

def online(request):
	template='temprature/online.html'
	results=Online.objects.all()
	context={
		'results':results,
	}
	return render(request,template,context)

def speedtest(request):
	template='temprature/speedtest.html'
	results=Speedtest.objects.all()
	context={
		'results':results,
	}
	return render(request,template,context)
