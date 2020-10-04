from django.shortcuts import render, redirect, reverse
from .models import Package
from .forms import PackageForm


def all_packages(request):
    """ A view to show all packages """

    packages = Package.objects.all()

    context = {
        'packages': packages,
    }

    return render(request, 'packages/packages.html', context)


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
