# Generated by Django 3.0.6 on 2020-05-25 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='media/image_user/noimage.png', upload_to='media/image_user')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.UserDate')),
            ],
        ),
    ]
