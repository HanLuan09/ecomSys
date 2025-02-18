# Generated by Django 4.1.13 on 2024-05-09 04:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_service', '0002_alter_mobile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('producer_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('des', models.TextField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='mobile',
            name='producer',
            field=models.ForeignKey(default='no', on_delete=django.db.models.deletion.CASCADE, to='mobile_service.producer'),
        ),
    ]
