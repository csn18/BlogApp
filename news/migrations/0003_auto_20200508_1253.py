# Generated by Django 3.0.6 on 2020-05-08 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20200508_1048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='category',
        ),
        migrations.DeleteModel(
            name='CategoryNews',
        ),
    ]
