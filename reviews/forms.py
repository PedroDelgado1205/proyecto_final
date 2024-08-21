from django import forms
from .models import Valoracion, Comentario

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Valoracion
        fields = ['contenido', 'calificacion', 'libro']  

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido', 'valoracion'] 
