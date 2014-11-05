"""
Logic for handling and interacting with companies
"""

from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

from shesays_platform.apps.utilities.view_utils import render_response
from shesays_platform.apps.analytics.scoring import get_shesays_score

from utils.forms import CompanyForm
from utils.api import CrunchbaseAPI
from models import Company

import logging
logger = logging.getLogger(__name__)

def display_companies(request):
    """ Displays all companies saved in our database """
    companies = Company.objects.all()
    return render_response(request, 'companies/companies_list.html', {'companies': companies})

def display_company(request, company_id):
    """ Displays a single company's profile page """
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist:
        # If no company exists with given id, redirect to home page
        return redirect('/')

    data = {
        'company': company,
        'score': get_shesays_score(company),
    }
    return render_response(request, 'companies/company_profile.html', data)

def search(request):
    """
    Searches for a company within our database.

    A company name to search for is expected in the request parameters.
    If a matching company is found, redirects to the company page.
    If no matching company exists, attempts to create the page by forwarding
    the request to create_company
    """
    params = request.GET
    company_name = params['q'].strip().lower()
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
    return render_response(request, 'companies/new_company.html', {'form': form})

@csrf_protect
def create_company(request):
    """ Creates a new company given form information """
    if request.method == 'POST':
        return _create_new_company(request.POST['name'])
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
        # Create the company using the name returned by crunchbase
        # TODO: We should add our own checks.. so a search for '*' doesn't give
        # back 'Google'
        # Or maybe we shouldn't let crunchbase spellcheck?
        new_company = Company(name=response['name'].lower())
        new_company.save()

        logger.info('New company created: {}'.format(response['name']))
        return redirect('/companies/{}'.format(new_company.id))
    else:
        return redirect('/')
