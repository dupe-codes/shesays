"""
Defines all models for saving user reviews
"""

from django.db import models
from shesays_platform.apps.companies.models import Company

class Review(models.Model):
    """ Represents a review for a company """
    content = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    sentiment_label = models.CharField(max_length=30, default='neutral')
    sentiment_score = models.FloatField(default=0)

    # Define a many-to-one relationship with companies
    company = models.ForeignKey(Company, related_name='reviews')

    def __unicode__(self):
        """ Defines a unicode string represenation of a review """
        return 'Review for {company}: {content}'.format(company=self.company.name, content=self.content)
