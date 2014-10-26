"""
Defines all models for saving user reviews
"""

from django.db import models
from shesays_platform.apps.companies.models import Company

class Review(models.Model):
    """ Represents a review for a company """
    content = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    company = models.ForeignKey(Company)

    def __unicode__(self):
        """ Defines a unicode string represenation of a review """
        return 'Review for {company}: {content}'.format(company=self.company.name, content=self.content)
