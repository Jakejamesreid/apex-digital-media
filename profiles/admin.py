from django.contrib import admin
from django.db import models
from django.forms import Textarea, TextInput

from services.models import Services
from website_details.models import Website

from .models import UserProfile


class WebsiteAdminInline(admin.TabularInline):
    extra = 0

    model = Website
    readonly_fields = ('id', 'user_profile',)

    list_display = (
        'id',
        'user_profile',
        'company_name',
        'company_description',
        'current_url',
        'new_site_description',
    )
    fields = (
        'id',
        'user_profile',
        'company_name',
        'company_description',
        'current_url',
        'new_site_description',
    )

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '40'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40})},
    }

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)


class ProfileLineItemAdminInline(admin.TabularInline):
    extra = 0

    model = Services

    readonly_fields = ('package', 'id')
    list_display = (
        'id',
        'remaining_pages',
        'remaining_email_addresses',
        'remaining_seo_updates',
        'remaining_website_updates',
    )
    fields = (
        'id',
        'package',
        'remaining_pages',
        'remaining_email_addresses',
        'remaining_seo_updates',
        'remaining_website_updates',
    )


class AdminProfile(admin.ModelAdmin):
    inlines = (ProfileLineItemAdminInline, WebsiteAdminInline,)


admin.site.register(UserProfile, AdminProfile)
