"""
Logic for handling and interacting with
companies
"""

from django.shortcuts import render_to_response
from models import Company

def display_company(request, company_id):
  """ Displays a single company's profile page """
  return render_to_response('companies/company_profile.html', {'company_id': company_id})

def search(request):
  params = request.GET
  import ipdb; ipdb.set_trace()
  return HttpResponseRedirect("")
