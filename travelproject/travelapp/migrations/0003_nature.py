# Generated by Django 3.2.3 on 2021-06-01 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_place_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='nature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=150)),
                ('img', models.ImageField(upload_to='picture')),
                ('desc', models.TextField()),
                ('heading', models.CharField(max_length=100)),
            ],
        ),
    ]
