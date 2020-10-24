from django.contrib import admin
from .models import Services


class ServicesAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = (
        'id',
        'profile',
        'package',
        'remaining_pages',
        'remaining_email_addresses',
        'remaining_seo_updates',
        'remaining_website_updates',
    )
    fields = (
        'id',
        'profile',
        'package',
        'remaining_pages',
        'remaining_email_addresses',
        'remaining_seo_updates',
        'remaining_website_updates',
    )


admin.site.register(Services, ServicesAdmin)
