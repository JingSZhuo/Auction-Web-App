# Generated by Django 4.1.3 on 2022-12-14 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction_app', '0005_alter_item_item_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.ImageField(default=None, height_field=50, max_length=1, null=True, upload_to='./auction_app_vue_frontend/src/Images', width_field=50),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_picture',
            field=models.CharField(max_length=254),
        ),
    ]
