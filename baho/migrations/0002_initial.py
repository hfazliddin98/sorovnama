# Generated by Django 4.2.7 on 2023-11-06 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('baho', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='oqtuvchi',
            name='kurs_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.kurs'),
        ),
        migrations.AddField(
            model_name='oqtuvchi',
            name='tur_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baho.turi'),
        ),
        migrations.AddField(
            model_name='fan',
            name='kurs_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.kurs'),
        ),
    ]