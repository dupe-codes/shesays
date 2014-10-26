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
    print 'Creating new company: ' + company_name
    return redirect('/')
