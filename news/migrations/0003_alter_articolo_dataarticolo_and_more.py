# Generated by Django 5.1.3 on 2025-02-12 08:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_articolo_options_alter_giornalista_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articolo',
            name='dataArticolo',
            field=models.DateField(db_default=datetime.datetime(2025, 2, 12, 9, 58, 18, 246363)),
        ),
        migrations.AlterField(
            model_name='giornalista',
            name='anno_di_nascita',
            field=models.DateField(db_default=datetime.datetime(2025, 2, 12, 9, 58, 18, 246363)),
        ),
    ]
