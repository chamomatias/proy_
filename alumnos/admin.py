from django.contrib import admin
from .models import Alumnos

@admin.register(Alumnos)
class AlumnosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'curso')
    search_fields = ('nombre', 'apellido', 'email')
    list_filter = ('curso',)
