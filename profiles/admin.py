from django.contrib import admin

from website_details.models import Website

from .models import ProfileLineItem, UserProfile


class WebsiteAdminInline(admin.TabularInline):
    extra = 0

    model = Website
    readonly_fields = ('user_profile',)

    list_display = ('id', 'user_profile', 'company_name',
                    'company_description', 'current_url',
                    'new_site_description',)
    fields = ('user_profile', 'company_name', 'company_description',
              'current_url', 'new_site_description',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)


class ProfileLineItemAdminInline(admin.TabularInline):
    extra = 0

    model = ProfileLineItem
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
