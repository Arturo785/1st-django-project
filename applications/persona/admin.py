from django.contrib import admin

# Register your models here.
from .models import Empleado, Habilidades

# Register your models here.

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "last_name",
        "job",
        "full_name",
        "id",
    )

    #We can make other tables with our own functions

    def full_name(self,obj):
        #obj is every object iterated on the admin
        return obj.name + " " + obj.last_name


    search_fields = ("name",)
    list_filter = ("job", "habilities",)

    filter_horizontal = ("habilities",)

admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Habilidades)