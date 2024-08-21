from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    genero = models.CharField(max_length=100)
    ano_publicacion = models.IntegerField()
    descripcion = models.TextField()
    portada = models.TextField()

    def __str__(self):
        return self.titulo
