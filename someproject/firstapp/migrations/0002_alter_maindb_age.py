# Generated by Django 4.2.6 on 2023-10-28 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maindb',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]