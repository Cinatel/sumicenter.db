from django.db import models

# Create your models here.


class productos(models.Model):
    id = models.AutoField(primary_key=True)
    modelo = models.CharField(max_length=100)
    serial = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)
    cantidad = models.CharField(max_length=100)
    EAN = models.CharField(max_length=100)
    fecha = models.DateField(null=False)
    orden =models.CharField(max_length=100 )
    factura =models.CharField(max_length=100 )

    class Meta:
        db_table = 'productos'

class truper(models.Model):
    id = models.AutoField(primary_key=True)
    modelo = models.CharField(max_length=100)
    serial = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)
    cantidad = models.CharField(max_length=100)
    EAN = models.CharField(max_length=100)
    fecha = models.DateField(null=False)
    orden =models.CharField(max_length=100 )
    factura =models.CharField(max_length=100 )

    class Meta:
        db_table = 'truper'


