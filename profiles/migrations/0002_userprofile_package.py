# Generated by Django 3.1.1 on 2020-10-16 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='package',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='services.services'),
        ),
    ]
