from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Alumnos
from .forms import AlumnosForm

class AlumnosRead(ListView):
    model = Alumnos
    template_name = 'alumnos/alumnos-leer.html'
    context_object_name = 'alumnos'

class AlumnosCreate(CreateView):
    model = Alumnos
    form_class = AlumnosForm
    template_name = 'alumnos/alumnos-crear.html'
    success_url = reverse_lazy('alumnos_lista')

class AlumnosUpdate(UpdateView):
    model = Alumnos
    form_class = AlumnosForm
    template_name = 'alumnos/alumnos-actualizar.html'
    success_url = reverse_lazy('alumnos_lista')

class AlumnosDelete(DeleteView):
    model = Alumnos
    template_name = 'alumnos/alumnos-borrar.html'
    success_url = reverse_lazy('alumnos_lista')

class AlumnosDetail(DetailView):
    model = Alumnos
    template_name = 'alumnos/alumnos-detallar.html'
