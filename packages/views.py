from django.shortcuts import render, get_object_or_404
from .models import Package


def all_packages(request):
    """ A view to show all packages """

    packages = Package.objects.all()

    context = {
        'packages': packages,
    }

    return render(request, 'packages/packages.html', context)


def package_detail(request, package_id):
    """ A view to show individual packages """

    package = get_object_or_404(Package, pk=package_id)
    context = {
        'package': package,
    }

    return render(request, 'packages/package_detail.html', context)
