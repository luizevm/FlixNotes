from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('obras/', ObrasView.as_view(), name='obras'),
    path('obras/criar/', ObraCreateView.as_view(), name='obra_create'),
    path('obras/<int:pk>/editar/', ObraUpdateView.as_view(), name='obra_update'),
    path('obras/<int:pk>/deletar/', ObraDeleteView.as_view(), name='obra_delete'),
    path('generos/', GenerosView.as_view(), name='generos'),
    path('plataformas/', PlataformasView.as_view(), name='plataformas'),
]