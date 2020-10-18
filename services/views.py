from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render, reverse

from profiles.models import UserProfile, ProfileLineItem
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
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = RequestServiceForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            print(request, 'Profile updated successfully')
        else:
            print(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = RequestServiceForm()
    orders = profile.orders.all()

    template = 'services/request-service.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)