from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, reverse

from profiles.models import UserProfile

from .forms import WebsiteForm


@login_required
def website_details(request):
    """ View and submit website details. """

    if request.method == 'POST':
        form = WebsiteForm(request.POST)
        if form.is_valid():
            profile = UserProfile.objects.get(user=request.user)
            website = form.save(commit=False)
            website.user_profile = profile
            website.save()
            messages.success(
                request, 'Website details have been successfully submitted.')
        else:
            messages.error(
                request, 'Update failed. Please ensure the form is valid.')

    form = WebsiteForm()

    context = {
        'form': form,
    }

    return render(request, 'website_details/website-details.html', context)
