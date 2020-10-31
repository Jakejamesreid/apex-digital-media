from django import forms
from phonenumber_field.formfields import PhoneNumberField


class ContactForm(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    from_email = forms.EmailField(required=True)
    contact_number = PhoneNumberField(region='IE')
    message = forms.CharField(widget=forms.Textarea, required=True)
