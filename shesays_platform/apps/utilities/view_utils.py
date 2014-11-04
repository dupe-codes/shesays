"""
Defines utility functions for use in rendering views
"""

from django.shortcuts import render_to_response
from django.template import RequestContext

def render_response(req, *args, **kwargs):
    """
    Wrapper for Django's render_to_response

    Ensures that the RequestContext is passed to the template
    """
    kwargs['context_instance'] = RequestContext(req)
    return render_to_response(*args, **kwargs)
