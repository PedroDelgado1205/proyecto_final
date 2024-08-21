from django.contrib import admin
from .models import Comentario, Valoracion
# Register your models here.

modelos = [Comentario, Valoracion]

admin.site.register(modelos)