# Generated by Django 3.0.4 on 2020-11-14 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_dynamic_password_validator'),
    ]

    operations = [
        migrations.AddField(
            model_name='dynamicpasswordvalidator',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
