from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import AuthorForm, CategoryForm, PostForm, SearchForm

def home(request) -> HttpResponse:
    """
    Vista para la página de inicio: muestra todos los posts.
    
    Args:
        request: Objeto HttpRequest.
    
    Returns:
        HttpResponse: Renderiza la plantilla home.html con la lista de posts.
    """
    try:
        posts = Post.objects.all()  # Estructura iterable (queryset)
        return render(request, 'blog/home.html', {'posts': posts})
    except Exception as e:
        return HttpResponse(f"Error al cargar posts: {str(e)}", status=500)

def create_author(request) -> HttpResponse:
    """
    Vista para crear un autor.
    
    Args:
        request: Objeto HttpRequest.
    
    Returns:
        HttpResponse: Renderiza el formulario o redirige a home tras guardar.
    """
    try:
        if request.method == 'POST':
            form = AuthorForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = AuthorForm()
        return render(request, 'blog/create_author.html', {'form': form})
    except Exception as e:
        return HttpResponse(f"Error al crear autor: {str(e)}", status=500)

def create_category(request) -> HttpResponse:
    """
    Vista para crear una categoría.
    
    Args:
        request: Objeto HttpRequest.
    
    Returns:
        HttpResponse: Renderiza el formulario o redirige a home tras guardar.
    """
    try:
        if request.method == 'POST':
            form = CategoryForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = CategoryForm()
        return render(request, 'blog/create_category.html', {'form': form})
    except Exception as e:
        return HttpResponse(f"Error al crear categoría: {str(e)}", status=500)

def create_post(request) -> HttpResponse:
    """
    Vista para crear un post.
    
    Args:
        request: Objeto HttpRequest.
    
    Returns:
        HttpResponse: Renderiza el formulario o redirige a home tras guardar.
    """
    try:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = PostForm()
        return render(request, 'blog/create_post.html', {'form': form})
    except Exception as e:
        return HttpResponse(f"Error al crear post: {str(e)}", status=500)

def search_posts(request) -> HttpResponse:
    """
    Vista para buscar posts por título.
    
    Args:
        request: Objeto HttpRequest.
    
    Returns:
        HttpResponse: Renderiza el formulario de búsqueda y resultados.
    """
    try:
        results = []
        if request.method == 'POST':
            form = SearchForm(request.POST)
            if form.is_valid():
                query = form.cleaned_data['query']
                results = Post.objects.filter(title__icontains=query)  # Estructura iterable
        else:
            form = SearchForm()
        return render(request, 'blog/search.html', {'form': form, 'results': results})
    except Exception as e:
        return HttpResponse(f"Error en búsqueda: {str(e)}", status=500)

def post_detail(request, post_id):
    """
    Vista para mostrar el detalle de un post individual.
    
    Args:
        request: Objeto HttpRequest.
        post_id: ID del post a mostrar.
    
    Returns:
        HttpResponse: Renderiza el template de detalle o error 404 si no existe.
    """
    try:
        post = Post.objects.get(id=post_id)
        return render(request, 'blog/post_detail.html', {'post': post})
    except Post.DoesNotExist:
        from django.http import Http404
        raise Http404("Post no encontrado")
    except Exception as e:
        return HttpResponse(f"Error al cargar post: {str(e)}", status=500)