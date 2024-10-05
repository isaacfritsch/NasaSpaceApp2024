from django.urls import path
from mapas import views



urlpatterns = [
    path('', views.mapas, name='mapas'),
    # path('mapas1/', views.mapas1, name='mapas1'),
    path('mapas2/', views.mapas2, name='mapas2'),
    path('mapas3/', views.mapas3, name='mapas3'),
    path('mapas4/', views.mapas4, name='mapas4'),    
]