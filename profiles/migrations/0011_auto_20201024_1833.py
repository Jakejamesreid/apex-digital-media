# Generated by Django 3.1.1 on 2020-10-24 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_auto_20201019_1924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilelineitem',
            name='remaining_email_addresses',
        ),
        migrations.RemoveField(
            model_name='profilelineitem',
            name='remaining_pages',
        ),
        migrations.RemoveField(
            model_name='profilelineitem',
            name='remaining_seo_updates',
        ),
        migrations.RemoveField(
            model_name='profilelineitem',
            name='remaining_website_updates',
        ),
    ]
