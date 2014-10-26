"""
Logic for handling and interacting with
companies
"""

from django.shortcuts import render_to_response, redirect
from models import Company
from django.views.decorators.csrf import csrf_exempt
#TODO: add csrf protection
from django.views.decorators.csrf import csrf_protect
from utils.forms import CompanyForm

def display_company(request, company_id):
  """ Displays a single company's profile page """
  return render_to_response('companies/company_profile.html', {'company_id': company_id})

def search(request):
  params = request.GET
  return HttpResponseRedirect("")

@csrf_exempt
def new_company(request):
    c = {}
    """ Renders view for creating a new company """
    form = CompanyForm()
    return render_to_response('companies/new_company.html', {'form': form}, c)

def create_company(request):
    """ Creates a new company given form information """
    c = {}
    if request.method == 'POST':
        parameters = request.POST
        new_company = Company(parameters)
        new_company.save()

        return redirect('/companies/{}'.format(new_company.id))
    else:
        return redirect('/')
