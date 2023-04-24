from django.shortcuts import render
from django.http import HttpResponse

tax_rate=15

# Create your views here.

def Tax(request):
    return render(request,"tax/index.html")


def calculate(request,number): 
    number=number+(number*(tax_rate/100))
    return render(request,"tax/tax_calculate.html",{"number":number})

def dispaly(request):
    return render(request,"tax/taxrate.html",{"tax_rate":tax_rate})