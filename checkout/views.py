from django.shortcuts import render, get_object_or_404
from packages.models import Package
from django.conf import settings

from .forms import OrderForm

import stripe


def checkout(request, package_id):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    order_form = OrderForm()
    template = 'checkout/checkout.html'

    package = get_object_or_404(Package, pk=package_id)
    total = round(package.price*100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=total,
        currency=settings.STRIPE_CURRENCY,
    )

    context = {
        'order_form': order_form,
        'package': package,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
