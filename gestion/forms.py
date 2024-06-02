from django import forms
from .models import Alumno,Curso,NotaAlumnoPorCurso

class AlumnoForm(forms.ModelForm):
    class Meta:
        model=Alumno
        fields = '__all__'
        
class CursoForm(forms.ModelForm):
    class Meta:
        model=Curso
        fields='__all__'

class NotaAlumnoPorCursoForm(forms.ModelForm):
    class Meta:
        model = NotaAlumnoPorCurso
        fields='__all__'