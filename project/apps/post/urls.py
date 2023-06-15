from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crear-anuncio', views.AnuncioCrear.as_view(), name='crear-anuncio'),
    # path('ver-anuncio', views.view_name.as_view(), name='ver-anuncio'),
]