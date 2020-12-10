from django.shortcuts import render, redirect
from .models import Cliente,Pedido

from .forms import ClienteForm, PedidoForm, CustomUserForm 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as do_logout

#from .forms import RegistroPersona

# Create your views here.

def home(request):
    clientes = Cliente.objects.all()
    data={
        'clientes': clientes 
    }
    return render(request, 'home.html',data)

def base(request):
    return render(request, 'base.html')    

def nuevo_cliente(request):
    return render(request, 'nuevo_cliente.html')


def calculadora(request):
    return render(request, 'calculadora.html')    

def crear_cliente(request):
    return render(request, 'clientes/crear_cliente.html')    

def listar_cliente(request):
    clientes = Cliente.objects.all()
    data={
        'clientes': clientes
        }
    return render(request, 'clientes/listar_cliente.html')     

def listar_pedidos(request):
    pedidos = Pedido.objects.all()
    data={
        'pedidos': pedidos
        }    
    return render(request, 'pedidos/listar_pedidos.html',data)    

def modificar_pedidos(request, id):
    pedidos= Pedido.objects.get(id=id)
    data = {
        'form': PedidoForm(instance=pedidos)
    }

    if request.method == 'POST':
        formulario = PedidoForm(data=request.POST, instance=pedidos) 
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Se ha modificado correctamente"
            return redirect(to="listar_pedidos.html")
        data["form"] = formulario        

    return render(request, 'pedidos/modificar_pedidos.html', data)    

def nuevo_pedido(request):
    data={
        'form':PedidoForm()
    }

    if request.method == 'POST':
        formulario=PedidoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Pedido registrado correctamente"
     
    return render(request, 'pedidos/nuevo_pedido.html',data)


def eliminar_pedidos(request, id):
    pedidos=Pedido.objects.get(id=id)
    pedidos.delete()
    return redirect(to="listar_pedidos.html")    

def login(request):
    return render(request, 'registration/login.html')    

def registrar(request):
    data = {
        'form':CustomUserForm()
    }

    if request.method=='POST':
        formulario=CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            #autentificar al usuario para redirigirlo al inicio
            formulario=formulario.cleaned_data['username']
            password=formulario.cleaned_data['password1']
            user=authenticate(username=username, password=password)
            login(request,user)
            return redirect(to='home.html/')
    return render(request, 'registration/registrar.html', data)   

def logout(request):
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')

def ubicacion(request):
    return render(request, 'ubicacion.html') 