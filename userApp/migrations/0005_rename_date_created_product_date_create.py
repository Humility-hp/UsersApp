# Generated by Django 5.0.3 on 2024-04-13 23:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0004_product_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='date_created',
            new_name='date_create',
        ),
    ]