from django.shortcuts import render
from . import forms
from . import models
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

def index(request):
    return render (request, "post/index.html")

class AnuncioCrear(CreateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = "post/crear-anuncio.html"


