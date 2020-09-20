from django.shortcuts import render, redirect, reverse, get_object_or_404
from packages.models import Package
from django.conf import settings

from .forms import OrderForm
from .models import Order

import stripe
import json


# package_id is default 0 for when payment form is submitted
def checkout(request, package_id):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    package = get_object_or_404(Package, pk=package_id)
    total = round(package.price)
    if request.method == 'POST':
        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
            'package': package,
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.package = package
            order.save()
            print("Order form is valid: ", order)
            return redirect(reverse(
                'checkout_success', args=[order.order_number]))
        else:
            print(request, 'There was an error with your form. \
                Please double check your information.')

    else:
        order_form = OrderForm()
        template = 'checkout/checkout.html'

        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=total*100,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()

    context = {
        'order_form': order_form,
        'package': package,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    order = get_object_or_404(Order, order_number=order_number)
    print(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
