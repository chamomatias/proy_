from django.urls import reverse_lazy
from django.views.generic import  TemplateView ,CreateView, ListView, UpdateView, DeleteView, DetailView
from .models import Cursos
from .forms import CursosForm


class InicioView(TemplateView):
    template_name = 'index.html'

# Crear curso
class CursoCreate(CreateView):
    model = Cursos
    form_class = CursosForm
    template_name = 'cursos/cursos-crear.html'
    success_url = reverse_lazy('cursos-leer')

# Listar cursos
class CursoRead(ListView):
    model = Cursos
    template_name = 'cursos/cursos-leer.html'
    context_object_name = 'cursos'

# Actualizar curso
class CursoUpdate(UpdateView):
    model = Cursos
    form_class = CursosForm
    template_name = 'cursos/cursos-actualizar.html'
    success_url = reverse_lazy('cursos-leer')

# Borrar curso
class CursoDelete(DeleteView):
    model = Cursos
    template_name = 'cursos/cursos-borrar.html'
    success_url = reverse_lazy('cursos-leer')

class CursoDetallar(DetailView):
    model = Cursos
    template_name = 'cursos/cursos-detallar.html'
    context_object_name = 'curso'