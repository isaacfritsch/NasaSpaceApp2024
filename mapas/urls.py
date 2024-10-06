from django.urls import path
from mapas import views



urlpatterns = [
    path('', views.home, name='home'),    
    path('mapas', views.mapas1, name='mapas1'),
    path('mapas2/', views.mapas2, name='mapas2'),
    path('mapas3/', views.mapas3, name='mapas3'),
    path('mapas4/', views.mapas4, name='mapas4'), 
    path('proxy/xeno-canto/', views.proxy_xeno_canto, name='proxy_xeno_canto'), 
    path('proxy/som/<int:recording_id>/', views.proxy_download_som, name='proxy_download_som'),
    path('api/get_plants_data/', views.get_plants_data, name='get_plants_data'),
    path('mapa_plantas/', views.mapa_plantas, name='mapa_plantas'),
    path('mapa_insetos/', views.mapa_insetos, name='mapa_insetos'),
    path('mapa_repteis/', views.mapa_repteis, name='mapa_repteis'),
    path('mapa_passaros/', views.mapa_passaros, name='mapa_passaros'),
    path('mapa_anfibios/', views.mapa_anfibios, name='mapa_anfibios'),

    
]