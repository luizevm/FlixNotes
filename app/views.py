from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from .models import *


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class ObrasView(View):
    def get(self, request, *args, **kwargs):
        obras = Obra.objects.all()
        return render(request, 'obras.html', {'obras': obras})


class GenerosView(View):
    def get(self, request, *args, **kwargs):
        generos = Genero.objects.all()
        return render(request, 'generos.html', {'generos': generos})


class PlataformasView(View):
    def get(self, request, *args, **kwargs):
        plataformas = Plataforma.objects.all()
        return render(request, 'plataformas.html', {'plataformas': plataformas})
