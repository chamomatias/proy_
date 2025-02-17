from django.urls import path
from .views import CursoRead, CursoCreate, CursoUpdate, CursoDelete, CursoDetallar

urlpatterns = [

    path('crear/', CursoCreate.as_view(), name='cursos-crear'),
    path('', CursoRead.as_view(), name='cursos-leer'),
    path('actualizar/<int:pk>/', CursoUpdate.as_view(), name='cursos-actualizar'),
    path('borrar/<int:pk>/', CursoDelete.as_view(), name='cursos-borrar'),
    path('detallar/<int:pk>/', CursoDetallar.as_view(), name='cursos-detallar'),

]
