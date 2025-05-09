from django.contrib import admin
from .models import Director, Pelicula

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    """
    Configuración del panel de administración para el modelo Director
    """
    list_display = ('nombre', 'nacionalidad', 'fecha_nacimiento')
    list_filter = ('nacionalidad',)
    search_fields = ('nombre', 'nacionalidad')
    ordering = ('nombre',)

@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    """
    Configuración del panel de administración para el modelo Pelicula
    """
    list_display = ('titulo', 'anio_estreno', 'director')
    list_filter = ('anio_estreno', 'director')
    search_fields = ('titulo',)
    ordering = ('titulo',)