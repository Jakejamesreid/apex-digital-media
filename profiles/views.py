from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings

from services.forms import RequestServiceForm

from .forms import UserProfileForm
from .models import ProfileLineItem, UserProfile


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def decrement_service(request, service_id, service_name):
    """ Decrement a particular service for a user. """
    if request.method == 'POST':
        profile = get_object_or_404(UserProfile, user=request.user)

        form = RequestServiceForm(request.POST)
        if form.is_valid():
            service = ProfileLineItem.objects.filter(
                profile=profile, id=service_id).values()
            if service[0][service_name] > 0:
                data = {
                    service_name: service[0][service_name]-1
                }
                ProfileLineItem.objects.filter(
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
