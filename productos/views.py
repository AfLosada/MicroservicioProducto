from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
from django.http import JsonResponse
from django.core import serializers

# Create your views here.

# Ver un producto
def productoGet(request, param):
    context = Producto.objects.get(pk = param)
    list = []
    list.append(context)
    return HttpResponse(serializers.serialize('json',list), content_type = 'application/json')

# Ver productos
@csrf_exempt
def productoList(request):
    template = 'productoList.html'
    context = Producto.objects.all()
    return  HttpResponse(serializers.serialize('json', context), content_type = 'application/json')

# Crear producto
def productoCreate(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            product = form.save()
            product.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Creación de producto exitosa')
            form = ProductoForm()
            context = {
                'form_producto': form
            }
            print('HOLA ESTOY VIVO')
            return HttpResponseRedirect(reverse(productoCreate))
        else:
            print('HOLA ESTOY DEAD')
            print(form.errors)
    else:
        form = ProductoForm()
        context = {
            'form_producto': form
        }
        print('HOLA ESTOY VIVO2')
        return render(request, 'productoCreate.html', context)

        
# Actualizar producto
@csrf_exempt
def productoComprar(request, id_producto, cantidad):
    producto = Producto.objects.get(pk = id_producto)
    producto.precio = producto.cantidad - cantidad
    producto.save()
    list = []
    list.append(producto)
    return HttpResponse(serializers.serialize('json',list), content_type = 'application/json')