# Generated by Django 3.0.6 on 2020-05-05 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('st', '0005_auto_20200505_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='text',
            field=models.TextField(),
        ),
    ]
