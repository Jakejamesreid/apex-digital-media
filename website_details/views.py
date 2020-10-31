from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from profiles.models import UserProfile

from .forms import SubmitWebsiteForm, UpdateWebsiteForm
from .models import Website


@login_required
def website_details(request, website_id=0):
    """ View and update website details. """

    profile = get_object_or_404(UserProfile, user=request.user)

    forms = []
    # Post request from the SUBMIT website form
    if request.method == 'POST' and 'submit-website' in request.POST:
        form = SubmitWebsiteForm(request.POST)
        if form.is_valid():
            profile = UserProfile.objects.get(user=request.user)
            website = form.save(commit=False)
            website.user_profile = profile
            website.save()
            messages.success(
                request, 'Website details have been successfully submitted.')
        else:
            for field in form:
                for error in field.errors:
                    messages.error(
                        request, f"Update failed. {error}")

    # Post request from the UPDATE website form
    elif request.method == 'POST' and 'update-website' in request.POST:
        website = Website.objects.get(
                user_profile=profile, id=website_id)
        form = UpdateWebsiteForm(request.POST, instance=website)
        if form.is_valid():
            website.save()
            messages.success(
                request, 'Website details have been successfully updated.')
        else:
            for field in form:
                for error in field.errors:
                    messages.error(
                        request, f"Update failed. {error}")

    # Get websites and append to a list
    websites = Website.objects.filter(user_profile=profile)
    if websites:
        for website in websites:
            forms.append(UpdateWebsiteForm(instance=website))

    context = {
        'forms': forms,
    }

    return render(request, 'website_details/update-website-details.html',
                  context)


@login_required
def submit_website_details(request):
    """ Submit website details. """

    form = SubmitWebsiteForm()
    context = {
        'form': form,
    }

    return render(request, 'website_details/submit-website-details.html',
                  context)
