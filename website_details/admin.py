from django.contrib import admin
from .models import Website


class WebsiteAdmin(admin.ModelAdmin):
    readonly_fields = ('user_profile',)

    list_display = (
        'id',
        'user_profile',
        'services',
        'company_name',
        'company_description',
        'current_url',
        'new_site_description',
    )
    fields = (
        'user_profile',
        'services',
        'company_name',
        'company_description',
        'current_url',
        'new_site_description',
    )


admin.site.register(Website, WebsiteAdmin)
