# Generated by Django 4.2.20 on 2025-04-30 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_cart'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
