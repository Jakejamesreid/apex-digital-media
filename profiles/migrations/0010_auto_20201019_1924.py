# Generated by Django 3.1.1 on 2020-10-19 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_auto_20201019_1915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilelineitem',
            name='services',
        ),
        migrations.AddField(
            model_name='profilelineitem',
            name='remaining_email_addresses',
            field=models.PositiveSmallIntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='profilelineitem',
            name='remaining_pages',
            field=models.PositiveSmallIntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='profilelineitem',
            name='remaining_seo_updates',
            field=models.PositiveSmallIntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='profilelineitem',
            name='remaining_website_updates',
            field=models.PositiveSmallIntegerField(default=0, null=True),
        ),
    ]
