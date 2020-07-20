from django import forms

from .models import Prueba

#aqui se personaliza el form que se despliega en el HTML

class PruebaForm(forms.ModelForm):

    class Meta:
        model = Prueba
        fields = (
            "titulo",
            "sub_titulo",
            "cantidad",
        )

        widgets ={
            'titulo': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese texto aqui'
                }
            ),
            'sub_titulo': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese texto aqui tambien gege'
                }
            ),
        }

    #Es necesario la palabra clean
    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']

        if cantidad < 10:
            raise forms.ValidationError("Pon mas de 10, puñetas")

        return cantidad