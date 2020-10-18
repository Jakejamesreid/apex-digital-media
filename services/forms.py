from django import forms
from profiles.models import UserProfile, ProfileLineItem


CHOICES= [
    ('new-page', 'New Page'),
    ('web-update', 'Website Update'),
    ('seo-update', 'SEO Update'),
    ('add-email', 'Add Email'),
]

class RequestServiceForm(forms.Form):
    services = forms.CharField(label='Please select the service', widget=forms.Select(choices=CHOICES))
    description = forms.CharField()

    description.widget.attrs['placeholder'] = 'Please describe the service you want.'
    description.widget.attrs['autofocus'] = True
    description.widget.attrs['class'] = (
            'border-black rounded-0 profile-form-input')

