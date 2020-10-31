from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client
from .models import Package


class TestViews(TestCase):

    def test_get_packages_view(self):
        response = self.client.get('/packages/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'packages/packages.html')

    def test_get_add_package_view(self):
        password = 'mypassword'
        my_admin = User.objects.create_superuser(
            'myuser', 'myemail@test.com', password)
        c = Client()
        c.login(username=my_admin.username, password=password)
        response = c.get('/packages/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'packages/add_package.html')

    def test_get_edit_package_view(self):
        password = 'mypassword'
        my_admin = User.objects.create_superuser(
            'myuser', 'myemail@test.com', password)
        c = Client()
        c.force_login(user=my_admin)

        package = Package.objects.create(
            name='Start Up',
            description='Test Package',
            features='Test Feature',
            price=100,
            currency='€',
        )

        response = c.get(f'/packages/edit/{package.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'packages/edit_package.html')

    def test_can_add_package(self):
        password = 'mypassword'
        my_admin = User.objects.create_superuser(
            'myuser', 'myemail@test.com', password)
        c = Client()
        c.force_login(user=my_admin)

        response = c.post('/packages/add/', {
            'name': 'Start Up',
            'description': 'Test Package',
            'features': 'Test Feature',
            'price': 100,
            'currency': '€',
        })
        self.assertRedirects(response, '/packages/')

    def test_can_edit_package(self):
        password = 'mypassword'
        my_admin = User.objects.create_superuser(
            'myuser', 'myemail@test.com', password)
        c = Client()
        c.force_login(user=my_admin)

        package = Package.objects.create(
            name='Start Up',
            description='Test Package',
            features='Test Feature',
            price=100,
            currency='€',
        )

        response = c.post(f'/packages/edit/{package.id}/', {
            'name': 'Executive',
            'description': 'Test Package',
            'features': 'Test Feature',
            'price': 100,
            'currency': '€',
        })
        self.assertRedirects(response, '/packages/')
        modified_package = Package.objects.filter(id=package.id)
        self.assertEqual(modified_package[0].name, 'Executive')

    def test_can_delete_package(self):
        password = 'mypassword'
        my_admin = User.objects.create_superuser(
            'myuser', 'myemail@test.com', password)
        c = Client()
        c.force_login(user=my_admin)

        package = Package.objects.create(
            name='Start Up',
            description='Test Package',
            features='Test Feature',
            price=100,
            currency='€',
        )

        response = c.post(f'/packages/delete/{package.id}/')
        self.assertRedirects(response, '/packages/')
        existing_packages = Package.objects.filter(id=package.id)
        self.assertEqual(len(existing_packages), 0)
