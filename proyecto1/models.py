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


# Create your models here.