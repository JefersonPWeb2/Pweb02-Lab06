from django.shortcuts import render, redirect
from .forms import AlumnoForm, CursoForm, NotaAlumnoPorCursoForm
from .models import Alumno, Curso, NotaAlumnoPorCurso

def nuevo_alumno(request):
    if request.method == "POST":
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_alumnos')
    else:
        form = AlumnoForm()
    return render(request, 'gestion/nuevo_alumno.html', {'form': form})

def nuevo_curso(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_cursos')
    else:
        form = CursoForm()
    return render(request, 'gestion/nuevo_curso.html', {'form': form})

def nueva_nota(request):
    if request.method == "POST":
        form = NotaAlumnoPorCursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_notas')
    else:
        form = NotaAlumnoPorCursoForm()
    return render(request, 'gestion/nueva_nota.html', {'form': form})

def lista_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'gestion/lista_alumnos.html', {'alumnos': alumnos})

def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'gestion/lista_cursos.html', {'cursos': cursos})

def lista_notas(request):
    notas = NotaAlumnoPorCurso.objects.all()
    return render(request, 'gestion/lista_notas.html', {'notas': notas})
