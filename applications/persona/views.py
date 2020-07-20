from django.shortcuts import render

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
)
from .models import Empleado

#Form de mi form personalizado
from.forms import EmployeeForm

from django.urls import reverse_lazy

class HomeView(TemplateView): #Vista encargada de mostrar la pagina de inicio
    template_name = "inicio.html"

class listAllEmployes(ListView):

    template_name = "persona/list__all_employes.html"
    model = Empleado  #trae todos los empleados
    paginate_by = 4
   # context_object_name = "empleados_list"

    #This works with the search input that its on the HTML 
    def get_queryset(self):
        key_word = self.request.GET.get("kword", "") #ese id lo puse yo 

        # if key_word == "":
        #     return Empleado.objects.all()   is one valid aproach

        return Empleado.objects.filter( name__icontains = key_word ) #if at least has one character of the Kword


class EditAllEmployees(ListView):

    template_name = "persona/edit_all_employes.html"
    model = Empleado  #trae todos los empleados
    paginate_by = 4
   # context_object_name = "empleados_list"

    #This works with the search input that its on the HTML 
    def get_queryset(self):
        key_word = self.request.GET.get("kword", "") #ese id lo puse yo 

        # if key_word == "":
        #     return Empleado.objects.all()   is one valid aproach

        return Empleado.objects.filter( name__icontains = key_word ) #if at least has one character of the Kword


class listEmployesByArea(ListView):
    
    template_name = "persona/list__all_by_area.html"

#metodo sobreescrito de la listView
    def get_queryset(self):
        area = self.kwargs["name"]
        return Empleado.objects.filter( department__name = area )


class listEmployesByJob(ListView):
    
    template_name = "persona/list__all_by_job.html"

    #metodo sobreescrito de la listView
    def get_queryset(self):
        jobQuery = self.kwargs["job"]
        return Empleado.objects.filter( job = jobQuery )

class listEmployesBykword(ListView):
    
    template_name = "persona/list__all_by_kword.html"

    #metodo sobreescrito de la listView
    def get_queryset(self):
        key_word = self.request.GET.get("kword", "") #ese id lo puse yo 
        return Empleado.objects.filter( name = key_word )

class listEmployesByHabilities(ListView):
    
    template_name = "persona/list__all_by_habilities.html"
    context_object_name = "habilidades"

    def get_queryset(self):
        key_word = self.request.GET.get("employee_search", "") #ese id lo puse yo 

        try:
            employee = Empleado.objects.get( name = key_word )
        except:
            print("No hubo request")
            return []

        return employee.habilities.all()

class EmployeDetailView(DetailView):
    model = Empleado
    template_name = "persona/employe_detail_view.html"

    # def get_context_data(self,**kwargs):
    #     context = super(EntryDetailView, self).get_context_data(**kwargs)
    #     context = ['Titulo'] = "Empleado del mes"
    #     return context

class SucessViewRegistration(TemplateView):
    template_name = "persona/success.html"

class EmployeCreateView(CreateView):
    model = Empleado
    template_name = "persona/create_employe_view.html"
    #fields = ['name','last_name','job','department','habilities','image',] ya no lo uso porque estoy usando forms
    #fields = ('__all__')
    #success_url = '.' #takes us to the same URL
    form_class = EmployeeForm
    success_url = reverse_lazy('persona_app:listAllEmployees')


    def form_valid(self,form): #This function is called when the data introduced into the template has beeen reconized as valid
        
        employee = form.save(commit = False)  #saves the data on the DB and assigns the data to this var , with commit False the save is aborted
        employee.full_name = employee.name + " " + employee.last_name
        employee.save() # updates the changes
        return super(EmployeCreateView,self).form_valid(form)

class UpdateEmployeView(UpdateView):
    model = Empleado
    template_name = "persona/update_view_employe.html"
    fields = ['name','last_name','job','department','habilities']
    success_url = reverse_lazy('persona_app:EditAllEmployees')


    #Antes de ser validados
    def post(self,request,*args,**kwargs):
        self.object = self.get_object()
        print(request.POST)
        return super().post(request,*args,**kwargs)

    #Despues de ser validados
    def form_valid(self,form): #This function is called when the data introduced into the template has beeen reconized as valid
        
        return super(UpdateEmployeView,self).form_valid(form)

class DeleteEmployeView(DeleteView):
    model = Empleado
    template_name = "persona/delete_employe_view.html"
    success_url = reverse_lazy('persona_app:EditAllEmployees')

    



 

