# TuPrimeraPagina+TuApellido
Este es mi primer proyecto web en Django, siguiendo el patrón MVT. Es un blog simple con autores, categorías y posts, incorporando buenas prácticas como type hints, docstrings, manejo de excepciones y validaciones.

## Instalación y Ejecución
1. Clona el repositorio: `git clone https://github.com/tuusuario/TuPrimeraPagina+TuApellido.git`
2. Instala dependencias: `pip install django`
3. Ejecuta migraciones: `python manage.py migrate`
4. (Opcional) Carga datos de prueba: `python manage.py shell < blog/init_data.py`
5. Corre el servidor: `python manage.py runserver`
6. Abre http://127.0.0.1:8000 en tu navegador.

## Orden de Pruebas y Funcionalidades
1. **Inicio**: Ve a la página principal para ver todos los posts (inicialmente vacía; usa init_data.py para datos de prueba).
2. **Crear Autor**: Crea al menos un autor (validaciones evitan campos vacíos o emails duplicados).
3. **Crear Categoría**: Crea al menos una categoría (validaciones evitan nombres vacíos).
4. **Crear Post**: Crea un post usando el autor y categoría creados (validaciones evitan títulos vacíos).
5. **Buscar**: Busca posts por título (validaciones evitan consultas vacías).
6. Repite para probar múltiples entradas. Todas las vistas incluyen manejo de errores.

Funcionalidades principales:
- Herencia de templates: Todos usan `base.html`.
- Formularios: Uno para cada modelo (con validaciones) y uno para búsqueda.
- BD: Almacena datos en SQLite con querysets iterables.
- Buenas prácticas: Type hints, docstrings, try-except, métodos de instancia en modelos.

## Mejoras Incorporadas
- **Type hints**: En funciones y clases para claridad.
- **Docstrings**: Documentación en todas las funciones/clases.
- **Excepciones**: Try-except en vistas para robustez.
- **Validaciones**: Campos no vacíos y unicidad en formularios.
- **Métodos de instancia**: Al menos 2 por modelo (ej: get_summary en Post).
- **Atributos de clase**: Compartidos en modelos (ej: DEFAULT_DISCOUNT).