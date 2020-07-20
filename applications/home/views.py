from django.shortcuts import render

from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
)

from .models import Prueba

from django.urls import reverse_lazy
from .forms import PruebaForm

#We are using based class views
# Create your views here.
class PruebaView(TemplateView): #Hereda de TemplateView
    template_name = 'home/prueba.html' #the view to renderize

class ResumenFundationView(TemplateView): #Hereda de TemplateView
    template_name = 'home/resumen_view.html' #the view to renderize

class TestListView(ListView): #Hereda de ListView
    template_name = 'home/lista.html'
    context_object_name = "listaNumeros"
    queryset = ['0' , '10' , '20' , '30']

class AddElementListView(CreateView): 
    template_name = 'home/add.html'
    model = Prueba

    form_class = PruebaForm
    success_url = '/'










