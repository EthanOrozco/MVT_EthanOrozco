from cmath import inf
import datetime
from urllib import request
from django.shortcuts import render, redirect  
from forms import *
from models import Curso, Familiar

# Create your views here.
def familiares(request):
    familiar1=Familiar (nombre= "César Orozco", edad=43, cumpleaños=datetime.date(1979, 6, 19))
    
    
    familiar2=Familiar (nombre= "Rocío Madrid", edad=43, cumpleaños=datetime.date(1979, 2, 3))
    
    
    familiar3=Familiar (nombre= "Jair Orozco", edad=15, cumpleaños=datetime.date(2007, 2, 14))
    

    contexto = {
        'familiar1': familiar1,
        'familiar2': familiar2,
        'familiar3': familiar3
    }

    return render(request, 'Familiares/familiares.html', contexto)

def inicio(request):
    
    return render(request, 'index.html')

def about(request):

    return render(request, 'About.html')

def herencias(request):

    return render(request, 'herencias.html')

def Formularios(request):

    contexto = {
        'form': Familia()
    }
    
    return render(request, 'formulario.html', contexto)

def curso_formulario(request):

    if request.method == 'POST':
        mi_formulario = CursoForm(request.POST)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data

            curso1 = Curso(nombre=data.get('nombre'), camada=data.get('camada'))
                
            curso1.save()

        return redirect('FamiliaresInicio')

    contexto = {
        'form': CursoForm()
}

    return render(request, 'cursoFormulario.html', contexto)

def busqueda_camada(request):
    
    contexto = {
        'form': BusquedaCamadaFormulario(),
    }

    return render(request, 'busqueda_camada.html', contexto)

def busqueda_camada_post(request):
    
    camada = request.GET.get('camada')

    cursos = Curso.objects.filter(camada__icontains=camada)
    contexto = {
        'cursos': cursos
    }

    return render(request, 'curso_filtrado.html', contexto)