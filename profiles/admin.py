from django.contrib import admin
from .models import UserProfile, ProfileLineItem


class ProfileLineItemAdminInline(admin.TabularInline):
    model = ProfileLineItem
    readonly_fields = ('package',)
    list_display = (
        'remaining_pages',
        'remaining_email_addresses',
        'remaining_seo_updates',
        'remaining_website_updates',
    )
    fields = (
        'package',
        'remaining_pages',
        'remaining_email_addresses',
        'remaining_seo_updates',
        'remaining_website_updates',
    )

    def get_extra(self, request, obj=None, **kwargs):
        extra = 0
        return extra


class AdminProfile(admin.ModelAdmin):
    inlines = (ProfileLineItemAdminInline,)


admin.site.register(UserProfile, AdminProfile)
