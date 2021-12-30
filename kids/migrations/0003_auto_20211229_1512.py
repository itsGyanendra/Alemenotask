# Generated by Django 3.1.4 on 2021-12-29 15:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kids', '0002_auto_20211229_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kid',
            name='parent_phone',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the format 9999999999.             Up to 10 digits', regex='^\\d{10}$')], verbose_name='Phone No.'),
        ),
    ]