# Generated by Django 3.2.2 on 2021-05-12 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ship_o_cereal', '0008_auto_20210512_1554'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addresses',
            name='countryId',
        ),
        migrations.AddField(
            model_name='addresses',
            name='country',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='Countries',
        ),
    ]
