from django.shortcuts import render, get_object_or_404
from packages.models import Package

from .forms import OrderForm


def checkout(request, package_id):
    order_form = OrderForm()
    template = 'checkout/checkout.html'

    package = get_object_or_404(Package, pk=package_id)

    context = {
        'order_form': order_form,
        'package': package,
    }

    return render(request, template, context)
