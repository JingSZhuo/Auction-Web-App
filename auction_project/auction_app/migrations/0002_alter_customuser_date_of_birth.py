# Generated by Django 4.1.3 on 2022-12-07 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
    ]