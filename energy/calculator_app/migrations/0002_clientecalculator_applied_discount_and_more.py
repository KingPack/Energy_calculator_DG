# Generated by Django 4.1.7 on 2023-03-17 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientecalculator',
            name='applied_discount',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='clientecalculator',
            name='coverage',
            field=models.FloatField(default=0),
        ),
    ]
