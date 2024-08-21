from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('add_review/<int:libro_id>/', views.add_review, name='add_review'),
    path('add_comment/<int:reseña_id>/', views.add_comment, name='add_comment'),
]
