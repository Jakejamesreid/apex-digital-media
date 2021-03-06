# Generated by Django 3.1.1 on 2020-10-16 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
        ('profiles', '0003_auto_20201016_1659'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileLineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lineitems', to='profiles.userprofile')),
                ('services', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.services')),
            ],
        ),
    ]
