"""
URL configuration for myblog project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # Incluye las URLs de la app blog
]
from django.conf import settings
from django.conf.urls.static import static

# ... (urlpatterns existente)

# Agrega esto al final para servir archivos media en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)