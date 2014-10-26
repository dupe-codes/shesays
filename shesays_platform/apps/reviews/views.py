"""
Logic for handling company reviews created by users.
"""

from django.shortcuts import render_to_response, redirect

def new_review(request, company_id):
    """ Renders view for creating a new review for given company """
    print 'Rendering view to create new review...'
    return render_to_response('reviews/new_review.html', {'company_id': company_id})

def create_review(request, company_id):
    """ Creates a new review for the given company """
    print 'Redirecting back to company ' + company_id
    # TODO: Figure out better way to handle redirects
    return redirect('/companies/{}'.format(company_id))

