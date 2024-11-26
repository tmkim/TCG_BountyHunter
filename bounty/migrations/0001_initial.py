# Generated by Django 5.1.3 on 2024-11-26 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bounties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_id', models.CharField(max_length=200)),
                ('card_name', models.CharField(max_length=200)),
                ('current_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
            ],
        ),
    ]
