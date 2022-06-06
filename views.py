from django.shortcuts import render
from .forms import ClienteForm

def MenuInicial(request):
    return render(request, 'app/MenuInicial.html')

def Categoria(request):
    return render(request, 'app/Categoria.html')

def seguimiento(request):
    return render(request, 'app/seguimiento.html')

def CarroCompra(request):
    return render(request, 'app/CarroCompra.html')

def Donaciones(request):
    return render(request, 'app/Donaciones.html')

def inicioSesion(request):
    return render(request, 'app/inicioSesion.html')

def registro(request):
    data = {
        'form': ClienteForm()
    }
    if request.method == 'POST':
        form = ClienteForm(data=request.POST)
        if form.is_valid():
            form.save()
            data["mensaje"]="Registro exitoso"
        else:
            data["mensaje"]="Error en el registro"
            data["form"]=form
            return redirect('/registro')
    return render(request, 'app/registro.html', data)
    
