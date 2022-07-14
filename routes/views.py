from os import set_inheritable
from django.shortcuts import render
from django.views.generic import ListView
from .models import Maps

# Create your views here.


class MapsView(ListView):
    queryset = Maps.objects.all()
