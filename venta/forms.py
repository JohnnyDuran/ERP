from django import forms
# App
from venta.models import Cliente, Producto, Venta

class ClienteForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super(ClienteForm, self).clean()
        return cleaned_data

    class Meta:
        model = Cliente
        fields = ['nombres', 'cedula', 'genero']
        widgets = {
            'nombres': forms.TextInput(attrs={'class':'form-control'}),
            'cedula': forms.TextInput(attrs={'class':'form-control'}),
            'genero': forms.Select(attrs={'class':'form-control'}),
        }


class ProductoForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super(ProductoForm, self).clean()
        return cleaned_data

    class Meta:
        model = Producto
        fields = ['descripcion', 'marca', 'precio']
        widgets = {
            'descripcion': forms.TextInput(attrs={'class':'form-control'}),
            'marca': forms.TextInput(attrs={'class':'form-control'}),
            'precio': forms.NumberInput(attrs={'class':'form-control','step':'.01'}),
        }


class VentaForm(forms.ModelForm):
    detalle_venta =  forms.CharField( required=True, widget =forms.HiddenInput(attrs={'class':'form-control'}))
    def clean(self):
        cleaned_data = super(VentaForm, self).clean()
        return cleaned_data


    class Meta:
        model = Venta
        fields = ['cliente', 'fecha', 'total']
        widgets = {
            'cliente': forms.Select(attrs={'class':'form-control'}),
            'fecha': forms.DateInput(attrs={'class':'form-control','type':'date'}),
            #'total': forms.HiddenInput(attrs={'class':'form-control','step':'.01'}),
        }
        exclude  = ['total']