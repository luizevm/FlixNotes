from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import *

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class ObrasView(View):
    def get(self, request, *args, **kwargs):
        obras = Obra.objects.all()
        return render(request, 'obras.html', {
            'obras': obras,
            'title': "Minhas Obras"
        })


class GenerosView(View):
    def get(self, request, *args, **kwargs):
        generos = Genero.objects.all()
        return render(request, 'generos.html', {'generos': generos})


class PlataformasView(View):
    def get(self, request, *args, **kwargs):
        plataformas = Plataforma.objects.all()
        return render(request, 'plataformas.html', {'plataformas': plataformas})


class ObraCreateView(CreateView):
    model = Obra
    template_name = "obra_form.html"
    fields = ["titulo", "tipo", "genero", "plataforma", "status", "nota", "comentario"]
    success_url = reverse_lazy("obras")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Adicionar Obra"
        return context


class ObraUpdateView(UpdateView):
    model = Obra
    template_name = "obra_form.html"
    fields = ["titulo", "tipo", "genero", "plataforma", "status", "nota", "comentario"]
    success_url = reverse_lazy("obras")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Editar Obra"
        return context


class ObraDeleteView(DeleteView):
    model = Obra
    template_name = "obra_confirm_delete.html"
    success_url = reverse_lazy("obras")
