from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render, reverse

from profiles.models import ProfileLineItem, UserProfile

from .forms import RequestServiceForm


@login_required
def services(request):
    """ View services available """
    if not request.user.is_superuser:
        messages.info(request, 'Sorry, only clients can do that.')
        return redirect(reverse('home'))

    profile = get_object_or_404(UserProfile, user=request.user)

    remaining_services = ProfileLineItem.objects.filter(profile=profile)
    context = {
        'remaining_services': remaining_services,
    }

    return render(request, 'services/services.html', context)



@login_required
def request_service(request):
    """ Display the request service form. """
    form = RequestServiceForm()

    template = 'services/request-service.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
