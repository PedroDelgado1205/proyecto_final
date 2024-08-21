from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm, CommentForm
from .models import Valoracion
from books.models import Libro

@login_required
def add_review(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.libro = libro
            review.usuario = request.user
            review.save()
            return redirect('books:detail', pk=libro_id)
    else:
        form = ReviewForm()
    return render(request, 'reviews/add_review.html', {'form': form, 'libro': libro})

@login_required
def add_comment(request, reseña_id):
    reseña = get_object_or_404(Review, id=reseña_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.reseña = reseña
            comment.usuario = request.user
            comment.save()
            return redirect('books:detail', pk=reseña.libro.id)
    else:
        form = CommentForm()
    return render(request, 'reviews/add_comment.html', {'form': form, 'reseña': reseña})
