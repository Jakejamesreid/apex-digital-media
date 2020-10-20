from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from .models import UserProfile, ProfileLineItem
from .forms import UserProfileForm
from services.forms import RequestServiceForm


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            print(request, 'Profile updated successfully')
        else:
            print(request, 'Update failed. Please ensure the form is valid.')
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
def decrement_service(request):
    """ Decrement a particular service for a user. """
    if request.method == 'POST':
        profile = get_object_or_404(UserProfile, user=request.user)
        remaining_services = ProfileLineItem.objects.filter(
            profile=profile).first()

        form = RequestServiceForm(request.POST)
        if form.is_valid():
            if form.data['services'] == 'new-page':
                if remaining_services.remaining_pages > 0:
                    remaining_services.remaining_pages -= 1

            if form.data['services'] == 'web-update':
                if remaining_services.remaining_website_updates > 0:
                    remaining_services.remaining_website_updates -= 1

            if form.data['services'] == 'seo-update':
                if remaining_services.remaining_seo_updates > 0:
                    remaining_services.remaining_seo_updates -= 1

            if form.data['services'] == 'add-email':
                if remaining_services.remaining_email_addresses > 0:
                    remaining_services.remaining_email_addresses -= 1

            remaining_services.save()
            print(request, 'Successfully updated sevices')
        else:
            print(request, 'Failed to update services')

    return redirect(reverse('services'))
