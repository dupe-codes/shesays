"""
Defines all urls associated with companies
"""

from django.conf.urls import patterns, include, url
import views

COMPANY_ID_PATTERN = '(?P<company_id>[1-9][0-9]*)'

urlpatterns = patterns('',

    # Displays a list of all companies
    url(r'^$', views.display_companies, name='display_companies'),

    # Displays a specific company
    url(r'{}/$'.format(COMPANY_ID_PATTERN), views.display_company, name='display_company'),

    #custom search url
    url('^search/$', views.search, name='company_search'),

    # Displays form for creating a new company
    # TODO: Replace this with mechanism of checking crunchbase for company info
    url(r'^new/$', views.new_company, name="new_company"),

    # Creates a new company given a POST request
    url(r'^create/$', views.create_company, name="create_company")
)
