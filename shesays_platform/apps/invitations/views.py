"""
Defines views for the email invitation system
"""

from django.shortcuts import redirect
from mailer import send_mail
from django.conf import settings

from shesays_platform.apps.utilities.view_utils import render_response
from .tasks import send_queued_emails

def new_invite(request):
    """ Renders the template for sending an invitation """
    return render_response(request, 'invitations/new_invitation.html')

def send_invite(request):
    """ Queues the email invite(s) to be sent """
    print 'Sending email...'

    # Send a silly test email
    send_mail('Hello', 'Hi, this is a test', settings.DEFAULT_FROM_EMAIL, ['njdupp@gmail.com'], fail_silently=False)
    send_queued_emails.delay()
    return redirect('/')
