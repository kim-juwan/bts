from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
import pandas as pd
import folium
import json
from folium.features import DivIcon
import cx_Oracle as oci
import matplotlib.pyplot as plt
import csv

def home(request):
    return render(request,'home.html')
@csrf_exempt
def index(request):
    if request.method == "GET":
        return render(request,'index.html')
    elif request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        with open('./QnA.csv','a',encoding='euc-kr',newline='') as fp:
            wr = csv.writer(fp, delimiter=',')
            wr.writerow([name,email,message])
        return render(request,'index.html')


def index2(request):
    return render(request,'index2.html')

def index3(request):
    return render(request,'index3.html')

def index4(request):
    return render(request,'index4.html')
