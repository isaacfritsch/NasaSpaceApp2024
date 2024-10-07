from django.urls import path
from mapas import views



urlpatterns = [
    path('', views.home, name='home'),    
    path('mapas1', views.mapas1, name='mapas1'),
    path('mapas2/', views.mapas2, name='mapas2'),
    path('mapas3/', views.mapas3, name='mapas3'),
    path('mapas4/', views.mapas4, name='mapas4'), 
    path('mapas5/', views.mapas5, name='mapas5'),
    path('mapas6/', views.mapas6, name='mapas6'),
    path('mapas7/', views.mapas7, name='mapas7'),
    path('proxy/xeno-canto/', views.proxy_xeno_canto, name='proxy_xeno_canto'), 
    path('proxy/som/<int:recording_id>/', views.proxy_download_som, name='proxy_download_som'),
    path('api/get_plants_data/', views.get_plants_data, name='get_plants_data'),
    

    
]