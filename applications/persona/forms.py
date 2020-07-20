from django import forms

from .models import Empleado

#Para dar un toque personalizado al crear un nuevo empleado

class EmployeeForm(forms.ModelForm):
    """Form definition for Employee."""

    class Meta:
        """Meta definition for Employeeform."""

        model = Empleado
        fields = (
            'name',
            'last_name',
            'job',
            'department',
            'image',
            'habilities',
        )

        widgets = {
            'habilities' : forms.CheckboxSelectMultiple()
        }
