# Generated by Django 4.0.4 on 2022-05-18 01:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('motorpool', '0015_brand_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiclepassport',
            name='auto',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pts', to='motorpool.auto', verbose_name='Автомобиль'),
        ),
    ]
