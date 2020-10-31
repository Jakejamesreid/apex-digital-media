from django.test import TestCase
from .forms import ContactForm


class TestContactForm(TestCase):

    def test_contact_first_name_is_required(self):
        form = ContactForm({"first_name": ""})
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors.keys())
        self.assertEqual(form.errors['first_name'][0],
                         'This field is required.')

    def test_contact_last_name_is_required(self):
        form = ContactForm({"last_name": ""})
        self.assertFalse(form.is_valid())
        self.assertIn('last_name', form.errors.keys())
        self.assertEqual(form.errors['last_name'][0],
                         'This field is required.')

    def test_contact_from_email_is_required(self):
        form = ContactForm({"from_email": ""})
        self.assertFalse(form.is_valid())
        self.assertIn('from_email', form.errors.keys())
        self.assertEqual(form.errors['from_email'][0],
                         'This field is required.')

    def test_contact_number_is_required(self):
        form = ContactForm({"contact_number": ""})
        self.assertFalse(form.is_valid())
        self.assertIn('contact_number', form.errors.keys())
        self.assertEqual(form.errors['contact_number'][0],
                         'This field is required.')

    def test_contact_message_is_required(self):
        form = ContactForm({"message": ""})
        self.assertFalse(form.is_valid())
        self.assertIn('message', form.errors.keys())
        self.assertEqual(form.errors['message'][0],
                         'This field is required.')

    def test_submit_contact_form(self):
        form = ContactForm({
            "first_name": "John",
            "last_name": "Doe",
            "from_email": "john.doe@gmail.com",
            "contact_number": "+353831457896",
            "message": "Test message",
        })
        self.assertTrue(form.is_valid())
