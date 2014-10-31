"""
Defines logic for rendering the home page
"""

from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext
from shesays_platform.apps.companies.models import Company 

def index(request):
  companies = Company.objects.all()
  return render_to_response('home/index.html', {'companies': companies}, context_instance =RequestContext(request))
