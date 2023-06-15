from django.contrib import admin
from . import models

# admin.site.register(models.Post)

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("titulo", "juego")


admin.site.register(models.NombreJuego)


