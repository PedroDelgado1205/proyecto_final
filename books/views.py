from django.shortcuts import render, get_object_or_404, redirect
from .models import Libro
from reviews.models import Valoracion
import requests
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'books/index.html')

def book_list(request):
    libros = Libro.objects.all()
    return render(request, 'books/book_list.html', {'libros': libros})

def book_detail(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    return render(request, 'books/book_detail.html', {'libro': libro})

def search_books(request):
    query = request.GET.get('q', '')
    if not query:
        return render(request, 'books/search.html', {'error': 'Por favor, proporciona el título del libro que deseas buscar.'})

    search_url = f'https://openlibrary.org/search.json?q={query}'
    response = requests.get(search_url)

    if response.status_code == 200:
        data = response.json()
        books = []

        for doc in data.get('docs', []):
            title = doc.get('title', 'Título no disponible')
            author = ', '.join(doc.get('author_name', [])) if doc.get('author_name') else 'Autor no disponible'
            ano_publicacion = doc.get('first_publish_year', 1)
            description = doc.get('first_sentence', ['Descripción no disponible'])[0]  # Tomar el primer elemento de la lista
            cover_id = doc.get('cover_i')
            genero = doc.get('subjet', '')

            # Construir URL para la página del libro y la portada
            book_url = f'https://openlibrary.org{doc.get("key", "")}'
            cover_url = f'https://covers.openlibrary.org/b/id/{cover_id}-L.jpg' if cover_id else None

            book_info = {
                'title': title,
                'author': author,
                'ano_publicacion': ano_publicacion,
                'description': description,
                'cover_url': cover_url,
                'url': book_url,
                'subjet': genero
            }
            books.append(book_info)

        return render(request, 'books/search.html', {'books': books})

    else:
        return render(request, 'books/search.html', {'error': 'Error al conectar con Open Library.'})

@login_required
def save_book(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        title = request.POST.get('title')
        print(title)
        author = request.POST.get('author')
        print(author)
        description = request.POST.get('description', '')
        print(description)
        cover = request.POST.get('cover_url', '')
        print(cover)
        ano_publicacion_str = request.POST.get('first_publish_year', '')
        print(ano_publicacion_str)
        genero = request.POST.get('subjet', '')
        print(genero)

        # Convertir ano_publicacion_str a entero, si es un número válido
        try:
            ano_publicacion = int(ano_publicacion_str) if ano_publicacion_str else None
        except ValueError:
            ano_publicacion = None

        # Crear un nuevo libro con los datos proporcionados
        libro = Libro(
            titulo=title,
            autor=author,
            genero=genero,
            ano_publicacion=ano_publicacion,
            descripcion=description,
            portada=f'https://covers.openlibrary.org/b/id/{cover}-L.jpg' if cover else None
        )
        libro.save()

        # Añadir el libro a la lista de libros leídos del usuario actual
        if libro not in request.user.perfilusuario.libros_leidos.all():
            request.user.perfilusuario.libros_leidos.add(libro)

        return redirect('books:book_detail', pk=libro.pk)

    return redirect('users:login')  # Redirigir al login si no está logueado
# Redirigir al login si no está logueado
