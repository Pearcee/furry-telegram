from django.urls import path
from . import views
from django.views.generic.base import TemplateView
from django.urls import path
from page.views import robots_txt

urlpatterns = [
    # ...
    path("robots.txt", robots_txt),
]

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('news', views.news, name='news'),
    path('test', views.test, name='test'),
    path("robots.txt", robots_txt),
]

""" 
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    ...
    (r'^robots\.txt$', direct_to_template,
     {'template': 'robots.txt', 'mimetype': 'text/plain'}),
)

    path('robots.txt',views.robots, name='robots', content_type="text/plain"),
 """