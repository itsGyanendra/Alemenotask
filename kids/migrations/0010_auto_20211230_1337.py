# Generated by Django 3.1.4 on 2021-12-30 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kids', '0009_auto_20211230_0634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_url',
            field=models.URLField(max_length=1000),
        ),
    ]