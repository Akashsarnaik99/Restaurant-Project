# Generated by Django 4.2.7 on 2023-11-24 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_fooditem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='price',
            field=models.IntegerField(max_length=50),
        ),
    ]
