from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
import csv

@csrf_exempt
def home(request):
    if request.method == "GET":
        return render(request,'home.html')
    elif request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        with open('./QnA.csv','a',encoding='euc-kr',newline='') as fp:
            wr = csv.writer(fp, delimiter=',')
            wr.writerow([name,email,message])
        return render(request,'home.html')


def ppt1(request):
    return render(request,'ppt1.html')

def ppt2(request):
    return render(request,'ppt2.html')
