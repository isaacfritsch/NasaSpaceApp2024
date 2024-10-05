from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import requests


def home(request): 
    return render(request, 'mapas/home.html')

def mapas1(request): 
    return render(request, 'mapas/mapas1.html')
def mapas2(request): 
    return render(request, 'mapas/mapas2.html')
def mapas3(request): 
    return render(request, 'mapas/mapas3.html')
def mapas4(request): 
    return render(request, 'mapas/mapas4.html')
def mapas5(request): 
    return render(request, 'mapas/mapas5.html')


def proxy_xeno_canto(request):
    # URL da API do Xeno-canto
    url = 'https://www.xeno-canto.org/api/2/recordings?query=cnt:Brazil'
    
    # Faz a requisição para a API do Xeno-canto
    response = requests.get(url)
    
    # Retorna a resposta JSON da API para o frontend
    return JsonResponse(response.json())

