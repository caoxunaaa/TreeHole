# Generated by Django 3.0.8 on 2020-07-17 08:35

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic', '0005_auto_20200716_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dynamic',
            name='text',
            field=ckeditor.fields.RichTextField(verbose_name='正文'),
        ),
    ]
