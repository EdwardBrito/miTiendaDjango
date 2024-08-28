from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Producto
from .forms import ProductoForm


# Create your views here.

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'tecnologia/lista_productos.html', {'productos': productos})

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Producto agregado exitosamente'}, status=200)
    else:
        form = ProductoForm()
    return render(request, 'tecnologia/agregar_producto.html', {'form': form})

@csrf_exempt
def eliminar_producto(request, id):
    if request.method == 'DELETE':
        producto = get_object_or_404(Producto, id=id)
        producto.delete()
        return JsonResponse({'message': 'Producto eliminado correctamente'}, status=200)
    return JsonResponse({'error': 'Método no permitido'}, status=405)