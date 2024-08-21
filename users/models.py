from django.db import models
from django.contrib.auth.models import User

class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='perfil_fotos/', blank=True, null=True)
    biografia = models.TextField(blank=True, null=True)
    libros_leidos = models.ManyToManyField('books.Libro', blank=True, related_name='usuarios_leidos')

    def __str__(self):
        return self.usuario.username