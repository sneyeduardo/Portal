from django.contrib import admin
from .models import Curso, Clase, Suscripcion

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'publicado')  # Cambiamos activo por publicado
    search_fields = ('titulo', 'descripcion_larga')
    list_filter = ('publicado',)            # Cambiamos activo por publicado
@admin.register(Clase)
class ClaseAdmin(admin.ModelAdmin):
    # Mostramos el orden y el ID del video directamente en la tabla
    list_display = ('titulo', 'curso', 'orden', 'vimeo_id')
    list_filter = ('curso',)
    search_fields = ('titulo', 'vimeo_id')
    ordering = ('curso', 'orden')

@admin.register(Suscripcion)
class SuscripcionAdmin(admin.ModelAdmin):
    # Control total sobre quién pagó y quién tiene acceso activo
    list_display = ('usuario', 'curso', 'fecha_compra', 'acceso_activo')
    list_filter = ('acceso_activo', 'curso')
    search_fields = ('usuario__username', 'curso__titulo')
