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
    Searches for a company given a user search query

    A company name to search for is expected in the request parameters.
    If a matching company is found in the db, redirects to the company page.
    If no matching company already exists, attempts to add the company to our db
    using the appropriate APIs
    """
    params = request.GET
    company_name = params['q'].strip().lower()
    try:
        # See if we have an exact match in the database already
        # If we do, great! cuts down on network traffic
        company = Company.objects.get(name=company_name)
        return redirect('/companies/{}/'.format(company.id))
    except Company.DoesNotExist:
        return _find_company(company_name)

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

def _find_company(company_name):
    """
    Queries the crunchbase API to find the given company
    """
    crunchbase = CrunchbaseAPI()
    response = crunchbase.get_company_info(company_name)
    if response['exists']:
        # grab and use the name given back by crunchbase
        company_name = response['name'].lower()
        try:
            # See if we already have an entry for the company
            company = Company.objects.get(name=company_name)
            return redirect('/companies/{}/'.format(company.id))
        except Company.DoesNotExist:
            new_company = Company(name=company_name)
            new_company.save()

            logger.info('New company created: {}'.format(company_name))
            return redirect('/companies/{}'.format(new_company.id))
    else:
        # Company doesn't exist, redirect to homepage
        return redirect('/')

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
        company_name = response['name'].lower()

        try:
            # If company already exists, redirect to it
            company = Company.objects.get(name=company_name)
            redirect('/companies/{}'.format(new_company.id))
        except Company.DoesNotExist:
            new_company = Company(name=company_name)
            new_company.save()

            logger.info('New company created: {}'.format(company_name))
            return redirect('/companies/{}'.format(new_company.id))
    else:
        return redirect('/')
