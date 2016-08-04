from .models import Url_Address
from django.shortcuts import render, get_object_or_404
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Create your views here.

def index(request):
    url_list = Url_Address.objects.all()
    return render(request, 'urlexpander/index.html', {'url_list' : url_list})

def expand(request):
	shorter_url = request.POST['shorter_url']
	html = urlopen(shorter_url)
	soup = BeautifulSoup(html, 'html.parser')
	url = Url_Address()
	url.short_url = shorter_url
	url.full_url = html.geturl()
	url.http_status = html.getcode()
	url.page_title = soup.html.head.title.contents[0]
	url.save()
	url_list = Url_Address.objects.all()
	return render(request, 'urlexpander/index.html', {'url_list' : url_list})

def delete(request, url_pk):
	url = get_object_or_404(Url_Address, pk=url_pk)
	url.delete()
	url_list = Url_Address.objects.all()
	return render(request, 'urlexpander/index.html', {'url_list' : url_list})
