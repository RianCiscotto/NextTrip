from django.shortcuts import render

# Create your views here.
from .models import Pais
from django.http import JsonResponse


def listar_paises(request):
    paises = Pais.objects.all().values()
    return JsonResponse(list[any](paises), safe=False)

def home(request):
    
    dados = list(Pais.objects.values('nome', 'populacao', 'curiosidade', 'status', 'bandeira'))
    return JsonResponse(dados, safe=False)