# TuPrimeraPagina+Rios
Este es mi primer proyecto web en Django, siguiendo el patrón MVT (Modelo-Vista-Template). Es un blog completo con autores, categorías y posts, incorporando buenas prácticas como type hints, docstrings, manejo de excepciones, validaciones, y extras como diseño con Bootstrap, imágenes en posts, una sección destacada y página de detalle para leer posts completos.

Descripción
El blog permite crear autores, categorías y posts (con imágenes opcionales), buscar posts por título, y leer el contenido completo de cada post. Incluye una sección destacada en la página de inicio con tips de viaje, y un diseño moderno y responsivo con Bootstrap.

Tecnologías Usadas
Django: Framework web para el backend y manejo de BD.
Bootstrap: Para el diseño frontend responsivo y moderno.
SQLite: Base de datos por defecto (fácil de usar en desarrollo).
Pillow: Librería para manejo de imágenes en posts (opcional).
Instalación y Ejecución
Clona el repositorio: git clone https://github.com/Giselarioss/TuPrimeraPagina-Rios.git
Navega a la carpeta: cd TuPrimeraPagina-Rios
Instala dependencias: pip install django pillow (Pillow es para imágenes).
Ejecuta migraciones: python manage.py migrate
(Opcional) Carga datos de prueba: python manage.py shell < blog/init_data.py
Corre el servidor: python manage.py runserver
Abre http://127.0.0.1:8000 en tu navegador.
Orden de Pruebas y Funcionalidades
Sigue este orden para probar todas las funcionalidades. Asegúrate de que el servidor esté corriendo.

Página de Inicio (http://127.0.0.1:8000/):

Verás una sección destacada con "NO TE PIERDAS Los mejores TIPS para viajar en comunidad" y una imagen de amigos viajando.
Debajo, una lista de posts recientes en tarjetas (si hay datos de prueba, verás un post sobre Londres). Si no hay posts, aparecerá "No hay posts aún".
Crear Autor (http://127.0.0.1:8000/create_author/):

Llena el formulario con nombre y email (ej: "Ana García", "ana@example.com").
Validaciones evitan campos vacíos o emails duplicados. Haz clic en "Guardar" y serás redirigido al inicio.
Crear Categoría (http://127.0.0.1:8000/create_category/):

Llena el formulario con un nombre (ej: "Viajes").
Validaciones evitan nombres vacíos. Haz clic en "Guardar".
Crear Post (http://127.0.0.1:8000/create_post/):

Selecciona autor y categoría creados.
Agrega título, contenido (ej: "Mi viaje a Londres", texto largo) e imagen opcional.
Validaciones evitan títulos vacíos. Haz clic en "Guardar"; el post aparecerá en la página de inicio.
Buscar Posts (http://127.0.0.1:8000/search/):

Ingresa un título parcial (ej: "Londres") y busca.
Verás resultados con título y resumen. Validaciones evitan consultas vacías.
Leer Post Completo:

Desde la página de inicio, haz clic en "Leer Más" en cualquier tarjeta.
Se abrirá la página de detalle (ej: /post/1/) con contenido completo, imagen y botón para volver.
Navegación General:

Usa el navbar responsivo para ir a cualquier página.
Prueba en móvil (F12 > Toggle device toolbar).
Funcionalidades Principales
Herencia de Templates: Todos los templates usan base.html con navbar y footer.
Formularios: Uno para cada modelo (autores, categorías, posts con imágenes) y uno para búsqueda, todos con validaciones y estilo Bootstrap.
BD: Almacena datos en SQLite con querysets iterables para listas eficientes.
Extras: Página de detalle para posts, sección destacada en home, imágenes subidas, diseño responsivo.
Mejoras Incorporadas
Type Hints: En funciones y clases para mayor claridad y mantenibilidad.
Docstrings: Documentación en todas las funciones, clases y métodos.
Excepciones: Bloques try-except en vistas para manejar errores (ej: posts no encontrados).
Validaciones: Campos no vacíos, unicidad de emails, y manejo de formularios en Django.
Métodos de Instancia: Al menos 2 por modelo (ej: get_summary() y is_recent() en Post).
Atributos de Clase: Compartidos en modelos (ej: DEFAULT_DISCOUNT en Author, MAX_POSTS en Category).
Diseño Moderno: Bootstrap para cards, navbar, botones y responsividad.
Estructura del Proyecto
myblog/: Configuración del proyecto Django (settings, URLs).
blog/: App principal con modelos, vistas, formularios, URLs y templates.
blog/templates/blog/: Templates HTML (base.html, home.html, etc.).
blog/static/blog/: Archivos estáticos (CSS, imágenes).
README.md: Este archivo.
Autor
Nombre: Gisela Rios
Curso: Python y Django
Fecha: Febrero 2026
Si encuentras errores, verifica que todas las dependencias estén instaladas y que los templates estén en la ruta correcta. ¡Disfruta explorando el blog!
