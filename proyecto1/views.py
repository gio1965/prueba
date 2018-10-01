from django.shortcuts import render
from .models import *

def home(request,template_name="proyecto1/home.html"):
	mensaje='Hello Word'
	#variable=tabla.consulta
	Alumnos= Alumno.objects.all()
	return render(request, template_name, locals(),)
# Create your views here.
