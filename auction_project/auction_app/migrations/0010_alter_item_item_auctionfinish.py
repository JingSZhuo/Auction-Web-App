# Generated by Django 4.1.3 on 2022-12-15 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction_app', '0009_alter_item_item_auctionfinish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_auctionfinish',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]