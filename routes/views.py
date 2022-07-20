from os import set_inheritable
from django.shortcuts import render
from django.views.generic import ListView
from . import models

# Create your views here.


class Home(ListView):
    model = models.Maps
