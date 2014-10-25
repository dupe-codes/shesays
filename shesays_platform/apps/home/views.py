"""
Defines logic for rendering the home page
"""

from django.shortcuts import render_to_response
from django.shortcuts import render

def index(request):
    return render_to_response('home/index.html')
