from django.db import models

# Create your models here.


# se crea el codigo python del modelo y la ORM se encarga de pasar todo eso a SQL
class Prueba(models.Model):
    titulo = models.CharField(max_length=20)
    sub_titulo = models.CharField(max_length=15)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.titulo


