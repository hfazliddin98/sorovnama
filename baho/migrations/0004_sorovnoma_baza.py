# Generated by Django 4.2.7 on 2023-11-08 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baho', '0003_baza'),
    ]

    operations = [
        migrations.AddField(
            model_name='sorovnoma',
            name='baza',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
