# Generated by Django 4.2.6 on 2023-12-09 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_alter_equipment_descr_alter_equipment_state_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentForUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('descr', models.CharField(blank=True, default='...', max_length=100, verbose_name='Описание')),
            ],
        ),
        migrations.RenameModel(
            old_name='Equipment',
            new_name='EquipmentNet',
        ),
        migrations.CreateModel(
            name='Workers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_and_initials', models.CharField(max_length=100, verbose_name='Имя')),
                ('department', models.CharField(max_length=100, verbose_name='Отдел')),
                ('number', models.IntegerField(verbose_name='Номер телефона')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('descr', models.CharField(blank=True, default='...', max_length=100, verbose_name='Заметки')),
                ('equip_on_worker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='firstapp.equipmentforusers')),
            ],
        ),
    ]