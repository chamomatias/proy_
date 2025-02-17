from django.db import models
from cursos.models import Cursos  # Importamos Cursos para la relación

class Alumnos(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    curso = models.ForeignKey(Cursos, on_delete=models.SET_NULL, null=True, blank=True, related_name='alumnos')

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.curso.nombre if self.curso else 'Sin curso'}"
