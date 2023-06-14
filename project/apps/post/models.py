from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=50)
    juego = models.ForeignKey('post.NombreJuego', null=False, on_delete=models.CASCADE)  
    rango = models.CharField(max_length=15, null=True)
    contenido = models.TextField
    fecha_de_publicacion = models.DateTimeField

    def __str__(self):
        return self.titulo
    
class NombreJuego(models.Model):
    nombre = models.CharField(max_length=20, unique=True, verbose_name='Juegos')

    def __str__(self):
        return self.nombre
    


