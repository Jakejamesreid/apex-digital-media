from django.contrib import admin
from .models import Package


class PackageAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'features',
        'price',
        'currency',
    )

    ordering = ('price',)


admin.site.register(Package, PackageAdmin)
