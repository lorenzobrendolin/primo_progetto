from django.db import models
from datetime import datetime

class Corso(models.Model):
    titolo = models.CharField(max_length=30)
    descrizione = models.TextField(max_length=90)
    data_inizio = models.DateField(db_default=datetime.now())
    data_fine = models.DateField(db_default=datetime.now())
    posti_disponibili = models.IntegerField(default=0,blank=True)

    def __str__(self):
        return self.titolo

    class Meta:
        verbose_name = "Corso"
        verbose_name_plural = "Corsi"
