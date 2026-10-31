from django.shortcuts import render

# Create your views here.

def home(request):
    res =render(request,'index.html')
    return res
