# Generated by Django 3.0.6 on 2020-05-05 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('st', '0003_auto_20200505_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='image',
            field=models.ImageField(upload_to='media/st'),
        ),
    ]
