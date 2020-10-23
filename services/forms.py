from django import forms


class RequestServiceForm(forms.Form):
    description = forms.CharField()

    description.widget.attrs['placeholder'] = \
        'Please describe the service you want.'
    description.widget.attrs['autofocus'] = True
    description.widget.attrs['class'] = (
            'border-black rounded-0 profile-form-input')
