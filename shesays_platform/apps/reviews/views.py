"""
Logic for handling company reviews created by users.
"""

from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from shesays_platform.apps.companies.models import Company
from models import Review
from utils.forms import ReviewForm
import settings

@login_required
@csrf_protect
def new_review(request, company_id):
    """ Renders view for creating a new review for given company """
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExit:
        # Redirect to home page if company with given id nonexistent
        redirect('/')

    form = ReviewForm()
    return render_to_response(
        'reviews/new_review.html',
        {'company': company, 'form': form},
        context_instance=RequestContext(request),
    )

@require_POST
@csrf_protect
def create_review(request, company_id):
    """
    Creates a new review for the given company

    The incoming request must be a POST request
    TODO: Need to add some validations here
    """
    company = Company.objects.get(id=company_id)
    review_fields = {
        'content': request.POST['content'],
        'sentiment_label': request.POST['sentiment'],
        'company': company,
    }

    review_fields['sentiment_score'] = _get_sentiment_score(review_fields['sentiment_label'])
    new_review = Review(**review_fields)
    new_review.save()

    # TODO: Figure out better way to handle redirects
    return redirect('/companies/{}'.format(company_id))

# ------------------------
# Review Helper Functions
# ------------------------

def _get_sentiment_score(sentiment_label):
    """
    Returns the numeric score for the given sentiment label.

    This just grabs the score assigned in the settings file. We could do something
    more complicated later
    """
    return settings.SENTIMENT_SCORES[sentiment_label]
