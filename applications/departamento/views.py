from django.shortcuts import render

from .forms import NewDepartmentForm
from .models import Departamento


from django.views.generic.edit import (
    FormView,
)

from django.views.generic import (
    ListView,
    DetailView,
)

from applications.persona.models import Empleado
from .models import Departamento

from django.urls import reverse_lazy

class NewDepartmentView(FormView):
    template_name = "departamento/new_department_add.html"
    form_class = NewDepartmentForm
    success_url = "/"

    def form_valid(self, form):
        #one way to create an object
        dept = Departamento(
            name = form.cleaned_data ["departamento"],
            short_name = form.cleaned_data ["shorname"] #The data from the forms that i did
        )
        dept.save()
        #if I use this way save is mandatory

        name = form.cleaned_data ["nombre"]
        last_name = form.cleaned_data ["apellido"]

        #ORM one way to create an object, .save() is not neccesary if using create
        Empleado.objects.create(
            name = name,
            last_name = last_name,
            job = '1',
            department = dept
        )

        return super(NewDepartmentView,self).form_valid(form)

class ListAllDepartments(ListView):
    template_name = "departamento/list_all_departments.html"
    model = Departamento
    paginate_by = 4

        #This works with the search input that its on the HTML 
    def get_queryset(self):
        key_word = self.request.GET.get("kword", "") #ese id lo puse yo 

        # if key_word == "":
        #     return Empleado.objects.all()   is one valid aproach

        return Departamento.objects.filter( name__icontains = key_word ) #if at least has one character of the Kword

class DepartmentDetailView(DetailView):
    model = Departamento
    template_name = "departamento/detail_departments.html"

