from django.db import models
from django.utils import timezone

# Create your models here.

class Url_Address(models.Model):
    short_url = models.CharField(max_length=50)
    full_url = models.CharField(max_length=250)
    http_status = models.TextField()
    page_title = models.TextField()
    created_date = models.DateTimeField('date created', default=timezone.now) 

    def __str__(self):
        return self.short_url
