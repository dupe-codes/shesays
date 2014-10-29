"""
Logic for handling and interacting with companies
"""

from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

from utils.forms import CompanyForm
from utils.api import CrunchbaseAPI
from models import Company

# TODO: Add logging (when new company created)

def display_companies(request):
    """ Displays all companies saved in our database """
    companies = Company.objects.all()
    return render_to_response('companies/companies_list.html', {'companies': companies})

def display_company(request, company_id):
    """ Displays a single company's profile page """
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist:
        # If no company exists with given id, redirect to home page
        return redirect('/')

    return render_to_response('companies/company_profile.html', {'company': company})

def search(request):
    """
    Searches for a company within our database.

    A company name to search for is expected in the request parameters.
    If a matching company is found, redirects to the company page.
    If no matching company exists, attempts to create the page by forwarding
    the request to create_company
    """
    params = request.GET
    company_name = params['q']
    try:
        company = Company.objects.get(name=company_name)
        return redirect('/companies/{}/'.format(company.id))
    except Company.DoesNotExist:
        return _create_new_company(company_name)

@login_required
@csrf_protect
def new_company(request):
    """ Renders view for creating a new company """
    form = CompanyForm()
    return render_to_response(
        'companies/new_company.html',
        {'form': form},
        context_instance=RequestContext(request),
    )

@csrf_protect
def create_company(request):
    """ Creates a new company given form information """
    if request.method == 'POST':
        # TODO: Figure out validations
        new_company = Company(name=request.POST['name'])
        new_company.save()
        return redirect('/companies/{}'.format(new_company.id))
    else:
        return redirect('/')

# ------------------------
# Company Helper Functions
# ------------------------

def _create_new_company(company_name):
    """
    Adds a new record for the given company name to our database.

    The plan is to use the crunchbase/glassdoor API to query for the given
    company name.
    If the calls return info on the company, happily add it
    to our database. If not, we'll assume the given company name is
    faulty, and return an appropriate message to the user.
    """
    crunchbase = CrunchbaseAPI()
    response = crunchbase.get_company_info(company_name)
    if response['exists']:
        new_company = Company(name=company_name)
        new_company.save()
        return redirect('/companies/{}'.format(new_company.id))
    else:
        return redirect('/')
