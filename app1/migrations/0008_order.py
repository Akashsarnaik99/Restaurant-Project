# Generated by Django 4.2.7 on 2023-11-29 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_fooditem_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('address', models.TextField(max_length=100)),
                ('pincode', models.IntegerField(max_length=100)),
                ('order_detail', models.TextField(max_length=100)),
                ('payment_mode', models.CharField(max_length=50)),
            ],
        ),
    ]