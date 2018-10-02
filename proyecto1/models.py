from django.db import models
from django.contrib.auth.models import User

class Alumno(models.Model):
	nombre = models.CharField('Nombre del alumno', max_length=60)
	apellidoPaterno = models.CharField(max_length=60)
	apellidoMaterno = models.CharField(max_length=60)
	edad = models.IntegerField(blank=False)
	fechaNacimiento = models.DateTimeField('Fecha de nacimiento', auto_now_add=False)
	def __str__(self):
		return str(self.nombre)+ " tiene la edad de " + str(self.edad)

class Estudiante(models.Model):
	nombre = models.CharField('Ingresa nombre', max_length=60)
	apellidoPaterno = models.CharField(max_length=60)
	apellidoMaterno = models.CharField(max_length=60)
	DNI = models.CharField(max_length=8)
	fechaNacimiento = models.DateField()
	sexos = (('F', 'Femenino'), ('M', 'Masculino'))
	sexo = models.CharField(max_length=1, choices=sexos, default='M')
	
	def NombreCompleto(self):
	cadena = "{0} {1}, {2}"

		return cadena.format(self.nombre, self.apellidoPaterno)

	def __str__(self):

		return self.NombreCompleto()

class Curso(models.Model):
	Nombre = models.CharField(max_length=50)
	Credito = models.PositiveSmallIntegerField()
	Estado = models.models.BooleanField(default=True)

	def __str__(self):

		return "{0} ({1})".format(self.Nombre, self,Credito)

class Matricula(models.Model):
	Estudiante = models.ForeignKey(Estudiante null=False, blank=False, on_delete=models.CASCADE)
	Curso = models.ForeignKey(Curso null=False, blank=False, on_delete=models.CASCADE)
	fechaMatricula = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		cadena = "{0} => {1}"
		return cadena.format(self.Estudiante, self.Curso.Nombre)
	
		
# Create your models here.