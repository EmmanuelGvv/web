
from django.urls import path
from . import views

urlpatterns = [
    # Login y registro
    path('login/', views.iniciar_sesion, name='login'),
    path('registro/', views.registro, name='registro'),
    path('logout/', views.cerrar_sesion, name='logout'),

    # Páginas de MusicStore
    path('', views.inicio, name='inicio'),
    path('categorias/', views.categorias, name='categorias'),
    path('viento/', views.viento, name='viento'),
    path('teclas/', views.teclas, name='teclas'),
    path('cuerdas/', views.cuerdas, name='cuerdas'),
    path('comprar/', views.comprar, name='comprar'),
]
