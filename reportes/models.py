from django.db import models

class Reporte(models.Model):
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    total_facturas = models.IntegerField()
    detalle_facturas = models.JSONField()  # Para almacenar los datos de las facturas como JSON
    fecha_generacion = models.DateTimeField(auto_now_add=True)  # Fecha de creación del reporte

    class Meta:
        db_table = 'reportes'
