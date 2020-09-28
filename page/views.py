from django.shortcuts import render
from django.core import serializers
from . models import Feed, Post
import json

from django.http import HttpResponse
from django.views.decorators.http import require_GET


# Create your views here.
def index(request):
	template='page/index.html'
	results=Feed.objects.all()
	context={
		'results':results,
	}
	return render(request,template,context)


def base_layout(request):
	template='page/base.html'
	return render(request,template)


# Create your views here.
def post_list(request):
    return render(request, 'page/index.html', {})

def about(request):
	template='page/about.html'
	return render(request,template)

def contact(request):
	template='page/contact.html'
	return render(request,template)	

def news(request):
	template='page/news.html'
	return render(request,template)

def test(request):
	template='page/test.html'
	return render(request,template)

def robots(request):
	template='page/robots.txt'
	return render(request,template)	

@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow: /private/",
        "Disallow: /junk/",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")