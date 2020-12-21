from django.urls import path
from . import views
from django.views.generic.base import TemplateView
from django.urls import path
from page.views import robots_txt

urlpatterns = [
    path('', views.index, name='index'),
]

