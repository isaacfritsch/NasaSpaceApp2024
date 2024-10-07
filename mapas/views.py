from django.shortcuts import render
from django.http import JsonResponse
import requests
from django.http import StreamingHttpResponse, JsonResponse

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
def mapas6(request): 
    return render(request, 'mapas/mapas6.html')
def mapas7(request): 
    return render(request, 'mapas/mapas7.html')

def proxy_xeno_canto(request):
    # URL da API do Xeno-canto
    url = 'https://www.xeno-canto.org/api/2/recordings?query=cnt:Brazil'
    
    # Faz a requisição para a API do Xeno-canto usando a biblioteca requests
    response = requests.get(url)
    
    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Retorna a resposta JSON da API para o frontend
        return JsonResponse(response.json())
    else:
        # Retorna um erro caso a requisição falhe
        return JsonResponse({'error': 'Falha ao buscar dados da API do Xeno-canto'}, status=response.status_code)
    
def proxy_download_som(request, recording_id):
    # URL do arquivo de som no Xeno-canto
    url = f'https://www.xeno-canto.org/{recording_id}/download'
    
    # Faz a requisição ao Xeno-canto para o arquivo de som
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            # Envia o áudio como uma resposta de streaming para o cliente
            return StreamingHttpResponse(response.iter_content(chunk_size=8192), content_type='audio/mpeg')
        else:
            return JsonResponse({'error': 'Falha ao baixar o som'}, status=response.status_code)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
import requests
from django.http import JsonResponse

def get_plants_data(request):
    # Exemplo com a API do GBIF para buscar plantas no Brasil com imagens
    url = 'https://api.gbif.org/v1/occurrence/search?country=BRA&taxonKey=6&hasCoordinate=true&mediaType=StillImage'
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        # Retorna os dados para o frontend
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Falha ao buscar dados'}, status=response.status_code)



