# Generated by Django 4.2.7 on 2023-11-24 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_alter_fooditem_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='image',
            field=models.ImageField(blank=True, upload_to='covers/'),
        ),
    ]
