# Generated by Django 4.2.6 on 2023-11-29 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('relevance', models.BooleanField()),
                ('slug', models.SlugField(blank=True, default='', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Men',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('second_name', models.CharField(blank=True, max_length=100)),
                ('age', models.IntegerField()),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('prof', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='firstapp.professions')),
            ],
        ),
    ]
