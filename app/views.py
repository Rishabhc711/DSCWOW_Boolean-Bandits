# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'app/index.html')

def about(request):
    return render(request,'app/about.html')

def visit(request):
    return render(request,'app/visit.html')

def tour(request):
    return render(request,'app/tour.html')   

def visual(request):
    return render(request,'app/visualise.html')    
