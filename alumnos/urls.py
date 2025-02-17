from django.urls import path
from .views import AlumnosRead, AlumnosCreate, AlumnosUpdate, AlumnosDelete, AlumnosDetail

urlpatterns = [
    path('', AlumnosRead.as_view(), name='alumnos_lista'),
    path('crear/', AlumnosCreate.as_view(), name='alumnos_crear'),
    path('<int:pk>/editar/', AlumnosUpdate.as_view(), name='alumnos_editar'),
    path('<int:pk>/eliminar/', AlumnosDelete.as_view(), name='alumnos_eliminar'),
    path('<int:pk>/detalle/', AlumnosDetail.as_view(), name='alumnos_detallar'),
]
