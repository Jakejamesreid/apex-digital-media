from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):

    readonly_fields = ('order_number', 'date',)

    fields = ('order_number', 'user_profile', 'date', 'first_name',
              'last_name', 'email', 'phone_number', 'country', 'postcode',
              'town_or_city', 'street_address1',
              'street_address2', 'county', 'package',
              'stripe_pid')

    list_display = ('order_number', 'date', 'first_name',
                    'last_name', 'package', 'stripe_pid')

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
