# Generated by Django 4.2.7 on 2023-11-09 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_kurs'),
        ('baho', '0006_alter_sorovnoma_baza'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('fan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baho.fanlar')),
                ('kurs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.kurs')),
            ],
        ),
        migrations.CreateModel(
            name='Oqituvchi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('fan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baho.fanlar')),
                ('kurs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.kurs')),
                ('tur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baho.turlar')),
            ],
        ),
        migrations.CreateModel(
            name='Fan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('kurs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.kurs')),
            ],
        ),
    ]
