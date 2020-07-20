from django import forms

from .models import Departamento


class NewDepartmentForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    departamento = forms.CharField(max_length=50)
    shorname = forms.CharField(max_length=20)