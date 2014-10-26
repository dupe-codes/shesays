"""
Logic for handling and interacting with
companies
"""

from django.shortcuts import render_to_response, redirect
from models import Company

def display_company(request, company_id):
  """ Displays a single company's profile page """
  return render_to_response('companies/company_profile.html', {'company_id': company_id})

def search(request):
  params = request.GET
  import pdb; pdb.set_trace();
  return HttpResponseRedirect("")

def new_company(request):
    """ Renders view for creating a new company """
    return render_to_response('companies/new_company.html')

def create_company(request):
    """ Creates a new company given form information """
    if request.method == 'POST':
        parameters = request.POST
        new_company = Company(parameters)
        new_company.save()

        return redirect('/companies/{}'.format(new_company.id))
    else:
        return redirect('/')
