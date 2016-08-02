from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from .models import Url_Address
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

# Create your views here.

def index(request):
    all_urls = Url_Address.objects.all()
    html = '<h1>Welcome to the URL expander</h1>'
    for url in all_urls:
        html = html + '<div><b>Page title</b> - ' + url.page_title + ' <br/><b>Short URL</b> - ' + url.short_url + ' <br/><b>Full or long URL</b> - ' + url.full_url + '</div><br>'
    return HttpResponse(html)

def post_url(request):
    if request.method == "POST":
    #    form = 
