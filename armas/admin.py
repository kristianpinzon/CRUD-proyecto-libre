from django.contrib import admin
from .models import CategoriaArma, ArmaDarkSouls, VideoDestacado

@admin.register(CategoriaArma)
class CategoriaArmaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)


@admin.register(VideoDestacado)
class VideoDestacadoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'activo')
    list_filter = ('activo',)
    search_fields = ('titulo',)
    list_editable = ('activo',)


@admin.register(ArmaDarkSouls)
class ArmaDarkSoulsAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'peso', 'daño_fisico', 'valor_almas', 'es_arma_de_jefe')
    list_filter = ('categoria', 'es_arma_de_jefe', 'escalado_fuerza')
    search_fields = ('nombre', 'descripcion', 'habilidad_especial', 'efecto_pasivo')
    list_editable = ('peso', 'daño_fisico', 'valor_almas')