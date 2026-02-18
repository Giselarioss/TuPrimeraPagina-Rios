"""
Script para inicializar datos de prueba en el blog.
Ejecutar con: python manage.py shell < blog/init_data.py
"""

from blog.models import Author, Category, Post

def main() -> None:
    """
    Función principal para crear datos de ejemplo.
    """
    try:
        # Crear autor de ejemplo
        author, created = Author.objects.get_or_create(name="Juan Pérez", email="juan@example.com")
        if created:
            print("Autor creado.")
        
        # Crear categoría de ejemplo
        category, created = Category.objects.get_or_create(name="Tecnología")
        if created:
            print("Categoría creada.")
        
        # Crear post de ejemplo
        post, created = Post.objects.get_or_create(
            title="Mi Primer Post",
            defaults={'content': "Hola mundo", 'author': author, 'category': category}
        )
        if created:
            print("Post creado.")
        
        print("Datos iniciales cargados exitosamente.")
    except Exception as e:
        print(f"Error al inicializar datos: {str(e)}")

if __name__ == "__main__":
    main()