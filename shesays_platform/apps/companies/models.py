"""
Defines the Company model and all of its associated functions.
"""

from django.db import models


class Company(models.Model):
    """ Model which represents a company in our database """
    name = models.CharField(max_length=30)

    def __unicode__(self):
        """ Return a string representation of the company """
        return self.name
