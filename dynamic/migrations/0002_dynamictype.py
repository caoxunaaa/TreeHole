# Generated by Django 3.0.8 on 2020-07-21 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DynamicType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(default='心情', max_length=10, verbose_name='类型名称')),
            ],
        ),
    ]