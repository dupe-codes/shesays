"""
Defines views for the email invitation system
"""

from django.shortcuts import redirect
from django.core.mail import send_mail
from django.conf import settings

from shesays_platform.apps.utilities.view_utils import render_response

def new_invite(request):
    """ Renders the template for sending an invitation """
    return render_response(request, 'invitations/new_invitation.html')

def send_invite(request):
    """ Queues the email invite(s) to be sent """
    print 'Sending email...'

    # Send a silly test email
    send_mail('Waddupp', 'Hi Sukhi,\nI just sent this from our app. How nifty.\n\n Best Regards,\nSheSaysCo',
        settings.DEFAULT_FROM_EMAIL, ['sgulati3@stanford.edu', 'njdupp@gmail.com'], fail_silently=False)
    return redirect('/')
