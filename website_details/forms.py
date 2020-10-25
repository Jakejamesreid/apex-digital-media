from django import forms
from .models import Website


class SubmitWebsiteForm(forms.ModelForm):

    class Meta:
        model = Website
        exclude = ('user_profile',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['company_name'].widget.attrs['autofocus'] = True
        self.fields['services'].label = "Available subscriptions"
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class UpdateWebsiteForm(forms.ModelForm):

    class Meta:
        model = Website
        exclude = ('user_profile',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['company_name'].widget.attrs['autofocus'] = True
        self.fields['services'].label = "Package"
        self.fields['services'].disabled = True
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
