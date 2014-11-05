"""
Defines urls for the email invitation system
"""

from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',

    # Render view for creating and sending a new invitation
    url(r'new/$', views.new_invite, name="new_invite"),

    # Endpoint for sending an email invitation
    url(r'send/$', views.send_invite, name="send_invite"),

)
