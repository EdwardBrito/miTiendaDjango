from django.db import models

# Create your models here.
# tecnologia/models.py

class Producto(models.Model):
    TIPO_PRODUCTO_CHOICES = [
        ('local', 'Local'),
        ('internacional', 'Internacional'),
    ]
    
    codigo = models.CharField(max_length=20, unique=True)
    descripcion = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=13, choices=TIPO_PRODUCTO_CHOICES)
    seleccionado = models.BooleanField(default=False)  # Nuevo campo para marcar selección
    
    def __str__(self):
        return f"{self.codigo} - {self.descripcion} - {self.tipo} - ${self.precio}"