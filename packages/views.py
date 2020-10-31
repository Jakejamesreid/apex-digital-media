from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib import messages

from .forms import PackageForm
from .models import Package


def all_packages(request):
    """ A view to show all packages. """

    packages = Package.objects.all()

    context = {
        'packages': packages,
    }

    return render(request, 'packages/packages.html', context)


@login_required
def add_package(request):
    """ Add a package to the store. """
    if not request.user.is_superuser:
        messages.info(request, 'Sorry, only admins can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PackageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added package!')
            return redirect(reverse('packages'))
        else:
            messages.error(
                request,
                'Failed to add package. Please ensure the form is valid.'
            )
    else:
        form = PackageForm()

    template = 'packages/add_package.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_package(request, package_id):
    """ Edit a package in the store. """
    if not request.user.is_superuser:
        messages.info(request, 'Sorry, only admins can do that.')
        return redirect(reverse('home'))

    package = get_object_or_404(Package, pk=package_id)
    if request.method == 'POST':
        form = PackageForm(request.POST, instance=package)
        if form.is_valid():
            package = form.save()
            messages.success(request, 'Successfully updated package!')
            return redirect(reverse('packages'))
        else:
            messages.error(
                request,
                'Failed to update package. Please ensure the form is valid.'
            )
    else:
        form = PackageForm(instance=package)
        messages.info(request, f'You are editing the {package.name} package')

    template = 'packages/edit_package.html'
    context = {
        'form': form,
        'package': package,
    }

    return render(request, template, context)


@login_required
def delete_package(request, package_id):
    """ Delete a package from the store. """
    if not request.user.is_superuser:
        messages.info(request, 'Sorry, only admins can do that.')
        return redirect(reverse('home'))

    package = get_object_or_404(Package, pk=package_id)
    package.delete()
    messages.success(request, 'Package deleted!')
    return redirect(reverse('packages'))
