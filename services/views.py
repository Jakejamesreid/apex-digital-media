from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render, reverse

from profiles.models import ProfileLineItem, UserProfile

from .forms import RequestServiceForm


@login_required
def services(request):
    """ View services available """
    if not request.user.is_superuser:
        print(request, 'Sorry, only clients can do that.')
        return redirect(reverse('home'))

    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()
    order = None
    for element in orders:
        order = element
        break

    print(order.package)
    # package = get_object_or_404(Package, pk=package_id)
    remaining_services = ProfileLineItem.objects.filter(profile=profile).first()
    context = {
        'order': order,
        'remaining_services': remaining_services,
    }

    print(request, 'Services')
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
