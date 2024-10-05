from django.urls import path
from mapas import views



urlpatterns = [
    path('', views.home, name='home'),    
    path('mapas', views.mapas1, name='mapas1'),
    path('mapas2/', views.mapas2, name='mapas2'),
    path('mapas3/', views.mapas3, name='mapas3'),
    path('mapas4/', views.mapas4, name='mapas4'), 
    path('proxy/xeno-canto/', views.proxy_xeno_canto, name='proxy_xeno_canto'),  
]