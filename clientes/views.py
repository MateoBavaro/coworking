from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import ClienteForm
from .models import Cliente


def lista_clientes(request):
    clientes = Cliente.objects.all().order_by('nombre')
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})


def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Cliente registrado con éxito!')
            return redirect('lista_clientes')
    else:
        form = ClienteForm()

    return render(request, 'clientes/crear_cliente.html', {'form': form})