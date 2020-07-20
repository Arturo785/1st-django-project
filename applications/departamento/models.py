from django.db import models

# Create your models here.
# se crea el codigo python del modelo y la ORM se encarga de pasar todo eso a SQL
class Departamento(models.Model):
    name = models.CharField("Nombre",max_length=20)
    short_name = models.CharField("Nombre corto",max_length=15)
    active = models.BooleanField("Activo", default= False)

    class Meta:
        verbose_name = "Mi departamento" #this is the responsible of showing on the admin console the name chosen
        verbose_name_plural = "Semos muchos deps" #this is the responsible of showing on the admin console the name chosen
        ordering = ["-name"]
        unique_together = ("name","short_name")


    def __str__(self):
        return "{}  : is active {}".format(self.name, self.active)

