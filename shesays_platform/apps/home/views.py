"""
Defines logic for rendering the home page
"""

from shesays_platform.apps.companies.models import Company
from shesays_platform.apps.utilities.view_utils import render_response

def index(request):
  companies = Company.objects.all()
  return render_response(request, 'home/index.html', {'companies': companies})
