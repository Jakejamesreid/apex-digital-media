from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Package
from .forms import PackageForm


def all_packages(request):
    """ A view to show all packages """

    packages = Package.objects.all()

    context = {
        'packages': packages,
    }

    return render(request, 'packages/packages.html', context)


@login_required
def add_package(request):
    """ Add a package to the store """
    if request.method == 'POST':
        form = PackageForm(request.POST)
        if form.is_valid():
            form.save()
            print(request, 'Successfully added package!')
            return redirect(reverse('add_package'))
        else:
            print(request, 'Failed to add package. Please ensure the form is valid.')
    else:
        form = PackageForm()

    template = 'packages/add_package.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_package(request, package_id):
    """ Edit a package in the store """
    if not request.user.is_superuser:
        print(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    package = get_object_or_404(Package, pk=package_id)
    if request.method == 'POST':
        form = PackageForm(request.POST, instance=package)
        if form.is_valid():
            package = form.save()
            print(request, 'Successfully updated package!')
            return redirect(reverse('packages'))
        else:
            print(request, 'Failed to update package. Please ensure the form is valid.')
    else:
        form = PackageForm(instance=package)
        print(request, f'You are editing {package.name}')

    template = 'packages/edit_package.html'
    context = {
        'form': form,
        'package': package,
    }

    return render(request, template, context)


@login_required
def delete_package(request, package_id):
    """ Delete a package from the store """
    if not request.user.is_superuser:
        print(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    package = get_object_or_404(Package, pk=package_id)
    package.delete()
    print(request, 'Package deleted!')
    return redirect(reverse('packages'))
