from django.conf import settings
from django.db import models
from django.utils import timezone


class Recetas(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	ingredients = models.TextField()
	instructions = models.TextField()
	preparation_time = models.IntegerField(help_text="Tiempo en minutos")
	cooking_time = models.IntegerField(help_text="Tiempo de coccion en minutos")
	servings = models.IntegerField(help_text="Numero de porciones")
	category = models.CharField(max_length=100, choices=[
		('breakfast', 'Desayuno'),
		('lunch', 'Almuerzo'),
		('dinner', 'Cena'),
		('dessert', 'Postre'),	
	])
	image = models.ImageField(upload_to='recipes/images/', blank=True)
	difficulty = models.CharField(max_length=20, choices=[
		('easy', 'Facil'),
		('medium', 'Medio'),
		('hard', 'Dificil'),
	])
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()

	def __str__(self):
		return self.title	

class Ingrediente(models.Model):
	# Atributos para cada ingrediente
	nombre = models.CharField(max_length=100)
	cantidad = models.CharField(max_length=50, help_text="Ej: 1 cucharada, 200ml")
	descripcion_especial = models.TextField(blank=True, help_text="Ej: opcional, solo si es nescesario")
	

	#Relacion con el modelo Recetas
	receta = models.ForeignKey(Recetas, on_delete=models.CASCADE, related_name="ingredientes")


	def __str__(self):
		return f"{self.cantidad} de {self.nombre}"	