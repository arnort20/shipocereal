# Generated by Django 3.2.2 on 2021-05-13 09:44

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ship_o_cereal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countries',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
