from django.contrib import admin
from .models import Services


class ServicesAdmin(admin.ModelAdmin):
    list_display = (
        'pages',
        'email_addresses',
        'seo_updates',
        'website_updates',
    )


admin.site.register(Services, ServicesAdmin)