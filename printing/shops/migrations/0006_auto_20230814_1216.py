# Generated by Django 3.0.5 on 2023-08-14 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0005_auto_20230811_2006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clients',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='clients',
            name='transaction',
        ),
        migrations.AddField(
            model_name='clients',
            name='amounts',
            field=models.TextField(default='[]'),
        ),
        migrations.AddField(
            model_name='clients',
            name='transactions',
            field=models.TextField(default='[]'),
        ),
    ]
