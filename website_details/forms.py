from django import forms
from .models import Website


class WebsiteForm(forms.ModelForm):

    class Meta:
        model = Website
        exclude = ('user_profile',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['company_name'].widget.attrs['autofocus'] = True
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
