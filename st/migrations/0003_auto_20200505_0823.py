# Generated by Django 3.0.6 on 2020-05-05 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('st', '0002_auto_20200505_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='text',
            field=models.TextField(max_length=4098),
        ),
    ]
