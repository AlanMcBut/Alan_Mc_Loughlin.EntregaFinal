from django.db import models
from datetime import datetime

class Post(models.Model):
    titulo = models.CharField(max_length=50, blank=False)
    juego = models.ForeignKey('post.NombreJuego', null=False, on_delete=models.CASCADE)  
    rango = models.CharField(max_length=15, null=True)
    cuenta_del_juego = models.CharField(max_length=50, blank=False, default='Ingrese su usuario del juego')
    contenido = models.TextField(max_length=200, default='Detalles sobre su peticion')
    fecha_de_publicacion = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.titulo
    
class NombreJuego(models.Model):
    nombre = models.CharField(max_length=20, unique=True, verbose_name='Juegos')

    def __str__(self):
        return self.nombre
    


