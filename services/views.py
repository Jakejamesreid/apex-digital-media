from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.template.loader import render_to_string

from profiles.models import UserProfile
from services.models import Services

from .forms import RequestServiceForm


@login_required
def services(request):
    """ View services available. """
    profile = get_object_or_404(UserProfile, user=request.user)
    remaining_services = Services.objects.filter(profile=profile)

    context = {
        'remaining_services': remaining_services,
        'service_name': ['remaining_pages', 'remaining_website_updates',
                         'remaining_email_addresses', 'remaining_seo_updates']
    }

    return render(request, 'services/services.html', context)


@login_required
def request_service(request, service_id, service_name):
    """ Display the request service form. """
    form = RequestServiceForm()

    template = 'services/request-service.html'

    context = {
        'form': form,
        'service_id': service_id,
        'service_name': service_name,
        'friendly_service_name': service_name.title().replace("_", " "),
    }

    return render(request, template, context)


@login_required
def decrement_service(request, service_id, service_name):
    """ Decrement a particular service for a user. """
    if request.method == 'POST':
        profile = get_object_or_404(UserProfile, user=request.user)

        form = RequestServiceForm(request.POST)
        if form.is_valid():
            service = Services.objects.filter(
                profile=profile, id=service_id).values()
            
            # Decrement Services object based on service_name
            if service[0][service_name] > 0:
                # service_name won't resolve with .update(service_name = val)
                # So store in a dict and call .update with dict
                data = {
                    service_name: service[0][service_name]-1
                }
                Services.objects.filter(
                    profile=profile, id=service_id).update(**data)

                subject = render_to_string(
                    'profiles/service_request_emails/email_subject.txt',
                    {'request': service_name.replace('_', ' ')})
                body = render_to_string(
                    'profiles/service_request_emails/email_body.txt', {
                        'user': profile.user,
                        'service_name': service_name,
                        'service_id': service_id,
                        'description': request.POST['description']
                    }
                )
                send_mail(
                    subject,
                    body,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.DEFAULT_FROM_EMAIL]
                )

            else:
                messages.error(request, 'You have used up this service.')
        else:
            messages.error(request, 'Form is invalid')

    return redirect(reverse('services'))
