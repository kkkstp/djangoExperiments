# Generated by Django 4.2.6 on 2023-12-03 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('descr', models.CharField(blank=True, max_length=100)),
                ('type', models.BooleanField(choices=[(0, 'Switch'), (1, 'Camera'), (2, 'Router')])),
            ],
        ),
    ]
