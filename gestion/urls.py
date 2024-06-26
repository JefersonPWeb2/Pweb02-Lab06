from django.urls import path
from . import views

urlpatterns = [
    path('nuevo_alumno/', views.nuevo_alumno, name='nuevo_alumno'),
    path('nuevo_curso/', views.nuevo_curso, name='nuevo_curso'),
    path('nueva_nota/', views.nueva_nota, name='nueva_nota'),
    path('lista_alumnos/', views.lista_alumnos, name='lista_alumnos'),
    path('lista_cursos/', views.lista_cursos, name='lista_cursos'),
    path('lista_notas/', views.lista_notas, name='lista_notas'),
]
