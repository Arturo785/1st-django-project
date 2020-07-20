from django.db import models

from applications.departamento.models import Departamento

from ckeditor.fields import RichTextField
# Create your models here.

class Habilidades(models.Model):

    hability = models.CharField("Habilidad",max_length=20)


    class Meta:
        verbose_name = "Habilidad" #this is the responsible of showing on the admin console the name chosen
        verbose_name_plural = "Habilidades empleados" #this is the responsible of showing on the admin console the name chosen


    def __str__(self):
        return self.hability



class Empleado(models.Model):
    jobs = (
        ("0", "Contador"),
        ("1", "Administrador"),
        ("2", "Economista"),
        ("3", "Otro"),
    )

    name = models.CharField("Nombre empleado",max_length=20)
    last_name = models.CharField("Apellido",max_length=15)
    full_name = models.CharField("Nombre completo",max_length=40,blank=True)
    job = models.CharField("Trabajo",max_length=2,choices=jobs)
    #LLave foranea con departamento
    department = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    #image = models.ImageField
    image = models.ImageField(upload_to="empleado",blank=True, null=True)

    #Because is a relation many to many * - *
    habilities = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()



    class Meta:
        verbose_name = "Persona" #this is the responsible of showing on the admin console the name chosen
        verbose_name_plural = "Personas" #this is the responsible of showing on the admin console the name chosen
        ordering = ["name"]


    def __str__(self):
        return "{}  de {}".format(self.name, self.department.name)


