from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import pandas as pd
import folium
import json
from folium.features import DivIcon
import cx_Oracle as oci
import matplotlib.pyplot as plt

def home(request):
    return render(request,'home.html')

def index(request):
    return render(request,'index.html')

def index2(request):
    return render(request,'index2.html')
