# Generated by Django 4.1.13 on 2024-05-13 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('type', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('sale', models.FloatField()),
                ('product_id', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=7)),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('total', models.FloatField()),
                ('status', models.BooleanField(default=False)),
                ('is_cancel', models.BooleanField(default=False)),
                ('order_items', models.ManyToManyField(to='order_service.orderitem')),
            ],
        ),
    ]
