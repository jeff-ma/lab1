from django.conf.urls import url
from . import views

urlpatterns =[
    # index / home page
    url(r'^$', views.index, name='index'),   
]
