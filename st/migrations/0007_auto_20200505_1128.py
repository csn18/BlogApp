# Generated by Django 3.0.6 on 2020-05-05 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('st', '0006_auto_20200505_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='title',
            field=models.CharField(max_length=128),
        ),
    ]