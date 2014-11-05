"""
Defines views for the email invitation system
"""

from django.shortcuts import redirect

from shesays_platform.apps.utilities.view_utils import render_response

def new_invite(request):
    """ Renders the template for sending an invitation """
    return render_response(request, 'invitations/new_invitation.html')

def send_invite(request):
    """ Queues the email invite(s) to be sent """
    print 'Sending email...'
    return redirect('/')
