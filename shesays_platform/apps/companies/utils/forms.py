"""
Defines form utilities for company views.
"""

from django import forms

class CompanyForm(forms.Form):
    """ Form for creating a new company. """
    name = forms.CharField(max_length=100)
