# Generated by Django 3.1.1 on 2020-10-14 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pages', models.PositiveSmallIntegerField(null=True)),
                ('email_addresses', models.PositiveSmallIntegerField(null=True)),
                ('seo_updates', models.PositiveSmallIntegerField(null=True)),
                ('website_updates', models.PositiveSmallIntegerField(null=True)),
            ],
        ),
    ]
