from django.contrib import admin
from .models import Cursos

@admin.register(Cursos)
class CursosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'fecha_inicio', 'fecha_fin', 'activo')  # Agregamos 'id'
    search_fields = ('nombre',)
    list_filter = ('activo',)
