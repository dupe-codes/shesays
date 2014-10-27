from django.conf.urls import patterns, include, url
from django.contrib import admin

# TODO: Add this to global settings module
COMPANY_ID_PATTERN = '(?P<company_id>[1-9][0-9]*)'

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),

    # url for rendering homepage
    url(r'^$', 'shesays_platform.apps.home.views.index'),

    # Add urls for user accounts
    url(r'^accounts/', include('account.urls')),

    # urls for rendering company views
    url(r'^companies/', include('shesays_platform.apps.companies.urls')),

    # urls for nested company reviews
    url(r'^companies/{}/reviews/'.format(COMPANY_ID_PATTERN), include('shesays_platform.apps.reviews.urls')),
)
