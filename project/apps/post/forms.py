from django import forms
from . import models

class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = '__all__'

class NombreJuegoForm(forms.ModelForm):
    class Meta:
        model = models.NombreJuego
        fields = '__all__'        