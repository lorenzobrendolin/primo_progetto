# Generated by Django 5.1.3 on 2025-02-12 09:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Corso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(max_length=30)),
                ('descrizione', models.TextField(max_length=90)),
                ('data_inizio', models.DateField(db_default=datetime.datetime(2025, 2, 12, 10, 25, 0, 535010))),
                ('data_fine', models.DateField(db_default=datetime.datetime(2025, 2, 12, 10, 25, 0, 535010))),
                ('posti_disponibili', models.IntegerField(blank=True, default=0)),
            ],
        ),
    ]
