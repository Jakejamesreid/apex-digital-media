# Generated by Django 3.1.1 on 2020-10-25 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_remove_services_website'),
        ('website_details', '0006_auto_20201025_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='services',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='services.services'),
        ),
    ]