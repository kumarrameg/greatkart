# Generated by Django 4.2.1 on 2023-06-03 04:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_variation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variation',
            old_name='cariation_value',
            new_name='variation_value',
        ),
    ]
