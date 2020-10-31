from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.conf import settings
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages


def index(request):
    """ A view to return the index page. """

    return render(request, 'home/index.html')


def contact(request):
    """ A view to render the contact page. """

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "New contact form submission."
            from_email = form.cleaned_data['from_email']
            body = render_to_string(
                'home/confirmation_emails/confirmation_email_body.txt',
                {
                    'first_name': form.cleaned_data['first_name'],
                    'last_name': form.cleaned_data['last_name'],
                    'from_email': from_email,
                    'contact_number': form.cleaned_data['contact_number'],
                    'message': form.cleaned_data['message'],
                }
            )
            try:
                send_mail(
                    subject,
                    body,
                    from_email,
                    [settings.DEFAULT_FROM_EMAIL]
                )
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, "Thank you for contacting us. \
                We will reply within 24 hours.")
            return redirect('home')
    return render(request, "home/contact.html", {'form': form})
