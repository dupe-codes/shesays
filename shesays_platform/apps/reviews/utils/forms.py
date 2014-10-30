"""
Defines form utilities for working with reviews
"""

from django.forms import Form, CharField, Textarea, ChoiceField, Select
from .. import settings #TODO: Replace this with import of django settings module

class ReviewForm(Form):
    """ form for creating a new review. """
    content = CharField(widget=Textarea(attrs={'placeholder': 'Add your review here'}))
    sentiment = ChoiceField(choices=((label,label) for label in settings.SENTIMENT_LABELS))
