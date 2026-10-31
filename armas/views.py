from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import CategoriaArma, ArmaDarkSouls, VideoDestacado
from .forms import ArmaDarkSoulsForm

# 1. LEER (Listar con filtro de categoría)
def index(request):
    categoria_id = request.GET.get('categoria')
    
    categorias = CategoriaArma.objects.all().order_by('nombre')
    videos_banner = VideoDestacado.objects.filter(activo=True)
    
    if categoria_id:
        armas = ArmaDarkSouls.objects.filter(categoria_id=categoria_id).select_related('categoria').order_by('nombre')
    else:
        armas = ArmaDarkSouls.objects.select_related('categoria').all().order_by('nombre')

    context = {
        'categorias': categorias,
        'videos_banner': videos_banner,
        'armas': armas,
        'categoria_seleccionada': categoria_id,
    }
    return render(request, 'armas/index.html', context)


def detalle_arma(request, pk):
    arma = get_object_or_404(ArmaDarkSouls.objects.select_related('categoria'), pk=pk)
    return render(request, 'armas/detalle_arma.html', {'arma': arma})


def añadir_arma(request):
    if request.method == 'POST':
        form = ArmaDarkSoulsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Arma guardada exitosamente')
            return redirect('index')
        else:
            messages.error(request, 'Error al guardar el arma. Revisa los datos.')
    else:
        form = ArmaDarkSoulsForm()

    return render(request, 'armas/formulario_arma.html', {
        'form': form,
        'titulo_pagina': 'Añadir Nueva Arma'
    })

def editar_arma(request, pk):
    arma = get_object_or_404(ArmaDarkSouls, pk=pk)
    
    if request.method == 'POST':
        form = ArmaDarkSoulsForm(request.POST, request.FILES, instance=arma)
        if form.is_valid():
            form.save()
            messages.success(request, 'Arma actualizada exitosamente')
            return redirect('index')  
        else:
            messages.error(request, 'Error al actualizar el arma.')
    else:
        form = ArmaDarkSoulsForm(instance=arma)

    return render(request, 'armas/formulario_arma.html', {
        'form': form,
        'titulo_pagina': f'Editar Arma: {arma.nombre}'
    })

def eliminar_arma(request, pk):
    arma = get_object_or_404(ArmaDarkSouls, pk=pk)
    
    if request.method == 'POST':
        nombre_arma = arma.nombre
        arma.delete()
        messages.success(request, f'El arma "{nombre_arma}" ha sido eliminada.')
        return redirect('index')

    return render(request, 'armas/confirmar_eliminar.html', {'arma': arma})