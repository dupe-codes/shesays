"""
Defines all urls for working with reviews.
"""

from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',

    # URL to render view to create a new review
    url(r'^new/$', views.new_review, name="new_review"),

    # URL to create a new company review
    url(r'^create/$', views.create_review, name="create_review"),
)
