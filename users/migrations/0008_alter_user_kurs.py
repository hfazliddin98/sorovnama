# Generated by Django 4.2.7 on 2023-11-09 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_user_kurs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='kurs',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='users.kurs'),
            preserve_default=False,
        ),
    ]
