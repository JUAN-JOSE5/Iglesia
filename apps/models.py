from django.db import models

class tabla (models.Model):
    Actividades = models.CharField(max_length=45)
    MantenimientoP = models.CharField(max_length=45)
    MantenimientoC = models.CharField(max_length=45)
    Fecha = models.DateField()
    FechaViso = models.DateField()

    def __str__(self):
        return self.Actividades
