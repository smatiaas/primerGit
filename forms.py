from django import forms
from.models import Cliente

class ClienteForm(forms.ModelForm):
    
    class Meta:
        model=Cliente
        fields = ['usuarioCliente', 'nombreCliente', 'contrasenaCliente', 'contrasenaCliente2', 'emailCliente', 'telefonoCliente', 'aceptoCliente']	
        