"""
Defines all urls associated with companies
"""

from django.conf.urls import patterns, include, url
import views

COMPANY_ID_PATTERN = '(?P<company_id>[1-9][0-9]*)'

urlpatterns = patterns('',

    url(r'{}/$'.format(COMPANY_ID_PATTERN), views.display_company, name='display_company'),
)
