# Generated by Django 3.2.2 on 2021-05-13 14:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ship_o_cereal', '0004_delete_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('orderId', models.BigAutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now=True)),
                ('addrId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ship_o_cereal.addresses')),
                ('cardId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ship_o_cereal.creditcards')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]