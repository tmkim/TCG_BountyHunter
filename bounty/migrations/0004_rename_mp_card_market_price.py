# Generated by Django 5.1.3 on 2024-12-02 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bounty', '0003_rename_card_color_card_color_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='mp',
            new_name='market_price',
        ),
    ]