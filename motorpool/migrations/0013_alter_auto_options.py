# Generated by Django 4.0.4 on 2022-05-13 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motorpool', '0012_alter_auto_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='options',
            field=models.ManyToManyField(related_name='cars', to='motorpool.option'),
        ),
    ]
