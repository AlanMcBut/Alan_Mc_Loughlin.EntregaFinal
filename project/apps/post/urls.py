from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crear-anuncio/', views.AnuncioCrear.as_view(), name='crear-anuncio'),
    path('lista-anuncios/', views.AnuncioLista.as_view(), name='lista-anuncios'),
    path('detalle-anuncio/<int:pk>/', views.AnuncioDetalle.as_view(), name='detalle-anuncio'),
    path('borrar-anuncio/<int:pk>/', views.AnuncioBorrar.as_view(), name='borrar-anuncio'),
    path('editar-anuncio/<int:pk>/', views.AnuncioEditar.as_view(), name='editar-anuncio'),
]