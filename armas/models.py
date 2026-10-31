from django.db import models

class CategoriaArma(models.Model):
    nombre = models.CharField(max_length=100, unique=True, help_text="Ej: Espadas rectas, Grandes espadas, Arcos")

    def __str__(self):
        return self.nombre


class VideoDestacado(models.Model):
    titulo = models.CharField(max_length=150, help_text="Título de la cinemática")
    archivo_video = models.FileField(upload_to='videos_destacados/', help_text="Sube un vídeo .mp4 para el banner rotativo")
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo


class ArmaDarkSouls(models.Model):
    nombre = models.CharField(max_length=150, unique=True)
    categoria = models.ForeignKey(CategoriaArma, on_delete=models.CASCADE, related_name='armas')
    descripcion = models.TextField(blank=True, null=True)
    peso = models.DecimalField(max_digits=4, decimal_places=1, help_text="Peso del arma (ej. 3.0, 12.5)")
    durabilidad = models.IntegerField(default=100)
    
    req_fuerza = models.PositiveIntegerField(default=0)
    req_destreza = models.PositiveIntegerField(default=0)
    req_inteligencia = models.PositiveIntegerField(default=0)
    req_fe = models.PositiveIntegerField(default=0)

    ESCALADO_CHOICES = [
        ('S', 'S'), 
        ('A', 'A'), 
        ('B', 'B'), 
        ('C', 'C'), 
        ('D', 'D'), 
        ('E', 'E'), 
        ('-', '-'),
    ]
    escalado_fuerza = models.CharField(max_length=1, choices=ESCALADO_CHOICES, default='-')
    escalado_destreza = models.CharField(max_length=1, choices=ESCALADO_CHOICES, default='-')
    escalado_inteligencia = models.CharField(max_length=1, choices=ESCALADO_CHOICES, default='-')
    escalado_fe = models.CharField(max_length=1, choices=ESCALADO_CHOICES, default='-')

    daño_fisico = models.PositiveIntegerField(default=0)
    daño_magico = models.PositiveIntegerField(default=0)
    daño_fuego = models.PositiveIntegerField(default=0)
    daño_rayo = models.PositiveIntegerField(default=0)
    daño_oscuro = models.PositiveIntegerField(default=0)

    habilidad_especial = models.CharField(max_length=150, blank=True, null=True)
    valor_almas = models.PositiveIntegerField(default=0)
    efecto_pasivo = models.CharField(max_length=100, blank=True, null=True)
    es_arma_de_jefe = models.BooleanField(default=False)

    imagen = models.ImageField(upload_to='armas_ds3/imagenes/', blank=True, null=True)
    video_habilidad_1 = models.FileField(upload_to='armas_ds3/videos/', blank=True, null=True)
    video_habilidad_2 = models.FileField(upload_to='armas_ds3/videos/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.categoria.nombre})"