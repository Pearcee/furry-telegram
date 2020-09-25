from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('news', views.news, name='news'),
    path(r'^robots\.txt$',
          TemplateView.as_view(template_name="robots.txt", 
          content_type="text/plain"),
    ),
]

""" 
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    ...
    (r'^robots\.txt$', direct_to_template,
     {'template': 'robots.txt', 'mimetype': 'text/plain'}),
)

 """