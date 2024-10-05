from django.shortcuts import render


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
