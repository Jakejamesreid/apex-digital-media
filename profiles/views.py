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
            service = ProfileLineItem.objects.filter(profile=profile, id=service_id).values()
            if service[0][service_name] > 0:
                data = {
                    service_name: service[0][service_name]-1
                }
                ProfileLineItem.objects.filter(profile=profile, id=service_id).update(**data)
            else:
                messages.error(request,
                                f'You have used up this service.')
        else:
            messages.error(request, 'Form is invalid')

    return redirect(reverse('services'))
