from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .forms import ReservaForm
from .models import Reserva


def crear_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Reserva creada exitosamente!')
            return redirect('lista_reservas')
    else:
        form = ReservaForm()

    return render(request, 'reservas/crear_reserva.html', {'form': form})


def lista_reservas(request):
    reservas = Reserva.objects.all().order_by('-fecha_inicio')
    return render(
        request, 'reservas/lista_reservas.html', {'reservas': reservas}
    )


def cancelar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)
    if request.method == 'POST':
        reserva.estado = 'cancelada'
        reserva.save()
        messages.warning(request, f'La reserva #{reserva.id} fue cancelada.')
    return redirect('lista_reservas')