from django.test import TestCase
from .forms import UpdateWebsiteForm


class TestContactForm(TestCase):

    def test_company_name_is_required(self):
        form = UpdateWebsiteForm({"company_name": ""})
        self.assertFalse(form.is_valid())
        self.assertIn('company_name', form.errors.keys())
        self.assertEqual(form.errors['company_name'][0],
                         'This field is required.')
