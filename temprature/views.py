from django.shortcuts import render
from django.core import serializers
from . models import Sensor
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