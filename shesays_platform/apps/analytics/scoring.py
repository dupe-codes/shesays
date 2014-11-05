"""
Contains functionality for implementing a
SheSays score for a company
"""

from django.db.models import Avg

from shesays_platform.apps.companies.models import Company

def get_shesays_score(company):
    """
    Calculates the shesays score for a given company.

    company: the django model object for the company

    Right now the score is just a simple aggregate of the sentiment
    scores of all reviews for the company. We can expand this and make it
    more powerful later.
    """
    reviews = company.reviews.all()
    aggregate_score = reviews.aggregate(Avg('sentiment_score'))
    avg_sentiment_score = aggregate_score['sentiment_score__avg']

    if avg_sentiment_score is None:
        return None
    else:
        # Return the score on a scale out of 100, rounded to 2 decimal points
        return round(avg_sentiment_score*100, 2)
