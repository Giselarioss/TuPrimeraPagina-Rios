from django.db import models

class Author(models.Model):
    """
    Modelo que representa a un autor de posts en el blog.
    
    Atributos:
        name (str): Nombre del autor.
        email (str): Correo electrónico único del autor.
    """
    name: str = models.CharField(max_length=100, help_text="Nombre del autor")
    email: str = models.EmailField(unique=True, help_text="Correo electrónico único")

    # Atributo de clase para un descuento compartido (ejemplo de buena práctica)
    DEFAULT_DISCOUNT: float = 0.0

    def __str__(self) -> str:
        """Retorna una representación legible del autor."""
        return self.name

    def get_full_info(self) -> str:
        """Método de instancia: Retorna información completa del autor."""
        return f"{self.name} ({self.email})"

    def apply_discount(self, amount: float) -> float:
        """Método de instancia: Aplica un descuento al monto dado."""
        return amount * (1 - self.DEFAULT_DISCOUNT)

class Category(models.Model):
    """
    Modelo que representa una categoría de posts.
    
    Atributos:
        name (str): Nombre único de la categoría.
    """
    name: str = models.CharField(max_length=100, unique=True, help_text="Nombre único de la categoría")

    # Atributo de clase para un límite compartido
    MAX_POSTS: int = 100

    def __str__(self) -> str:
        """Retorna una representación legible de la categoría."""
        return self.name

    def get_post_count(self) -> int:
        """Método de instancia: Retorna el número de posts en esta categoría."""
        return self.post_set.count()

    def is_full(self) -> bool:
        """Método de instancia: Verifica si la categoría ha alcanzado el límite de posts."""
        return self.get_post_count() >= self.MAX_POSTS

class Post(models.Model):
    """
    Modelo que representa un post en el blog.
    
    Atributos:
        title (str): Título del post.
        content (str): Contenido del post.
        author (Author): Autor del post (relación ForeignKey).
        category (Category): Categoría del post (relación ForeignKey).
        published_date (datetime): Fecha de publicación automática.
    """
    image = models.ImageField(upload_to='posts/', blank=True, null=True, help_text="Imagen opcional del post")
    title: str = models.CharField(max_length=200, help_text="Título del post")
    content: str = models.TextField(help_text="Contenido del post")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, help_text="Autor del post")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, help_text="Categoría del post")
    published_date = models.DateTimeField(auto_now_add=True, help_text="Fecha de publicación")

    def __str__(self) -> str:
        """Retorna una representación legible del post."""
        return self.title

    def get_summary(self, words: int = 20) -> str:
        """Método de instancia: Retorna un resumen del contenido."""
        return ' '.join(self.content.split()[:words]) + '...'

    def is_recent(self, days: int = 7) -> bool:
        """Método de instancia: Verifica si el post es reciente (últimos X días)."""
        from django.utils import timezone
        return (timezone.now() - self.published_date).days <= days