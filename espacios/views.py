from django.shortcuts import render
from .models import Espacio

def lista_espacios(request):
    espacios = Espacio.objects.filter(disponible=True)
    return render(request, 'espacios/lista_espacios.html', {'espacios': espacios})