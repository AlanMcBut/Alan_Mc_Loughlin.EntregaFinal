from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crear-anuncio/', views.AnuncioCrear.as_view(), name='crear-anuncio'),
    path('lista-anuncios/', views.AnuncioLista.as_view(), name='lista-anuncios'),
]