from django.db import models
from django.urls import reverse_lazy
from django.views import generic
from django.utils import timezone
import datetime


class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    creation_date = models.DateTimeField("date published", auto_now_add = True)
    
    def __str__(self):
        return self.title
    
