from django import forms 
from django.forms import ModelForm
from .models import Cliente
from .models import Pedido
from django.contrib.auth.forms import UserCreationForm


class ClienteForm(ModelForm):
    class Meta:
        model=Cliente
        fields=['nombre', 'rut', 'email', 'direccion', 'telefono']

class PedidoForm(ModelForm):
    class Meta:
        model=Pedido
        fields=['articulo','descripcion','precio','cliente']

class CustomUserForm(UserCreationForm):
    pass    

