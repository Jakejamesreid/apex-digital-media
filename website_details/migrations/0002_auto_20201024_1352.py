# Generated by Django 3.1.1 on 2020-10-24 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_details', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='current_url',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]