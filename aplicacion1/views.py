from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def Jvconsultacontroller (request):
   return HttpResponse ('Pàgina Aplicació Demo Python 3.5!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

def Question (request):
   return HttpResponse('Salida Question')

def Choice (request):
   return HttpResponse('Salida Choice')

def Sensor (request):
   return HttpResponse('Salida Sensor')

def Tipo_Sensor (request):
   return HttpResponse('Salida Tipo_Sensor')

def Componente (request):
    return HttpResponse('Salida Componente')

def Ubicacion (request):
    return HttpResponse('Salida Ubicacion')

def Servicio (request):
    return HttpResponse('Salida Servicio')

def Usuario (request):
    return HttpResponse('Salida Usuario')