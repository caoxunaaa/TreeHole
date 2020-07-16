# Generated by Django 3.0.8 on 2020-07-16 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic', '0004_auto_20200712_1030'),
    ]

    operations = [
        migrations.AddField(
            model_name='dynamictype',
            name='mood_type',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='心情类型'),
        ),
        migrations.AlterField(
            model_name='dynamictype',
            name='type_name',
            field=models.CharField(default='心情', max_length=10, verbose_name='类型名称'),
        ),
    ]