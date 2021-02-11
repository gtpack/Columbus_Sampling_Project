from django.shortcuts import render
import pandas

def home(request):

    return render(request,"home.html")
