from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class PerfilEstudiante(models.Model):
    """Extensión del usuario por defecto de Django para guardar datos extra del alumno"""
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    telefono = models.CharField(max_length=20, blank=True, null=True)
    pais_o_ciudad = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return f"Perfil de {self.usuario.username}"

class Curso(models.Model):
    """Información general del curso"""
    titulo = models.CharField(max_length=200)
    descripcion_corta = models.CharField(max_length=255)
    descripcion_larga = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    publicado = models.BooleanField(default=True, help_text="Desmarcar para ocultar el curso del portal")
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Clase(models.Model):
    """Cada uno de los videos/módulos que pertenecen a un curso"""
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='clases')
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    vimeo_id = models.CharField(max_length=100, help_text="ID de seguridad del video en Vimeo")
    orden = models.PositiveIntegerField(help_text="Ej: 1 para la primera clase")
    fecha_estreno = models.DateTimeField(help_text="Fecha y hora en la que se libera el video (Ej: Viernes 8:00 PM)")
    duracion = models.CharField(max_length=20, help_text="Ej: 2h 30m")

    class Meta:
        ordering = ['curso', 'orden']
        unique_together = ('curso', 'orden') # Evita que hayan dos "Clase 1" en el mismo curso

    def __str__(self):
        return f"{self.curso.titulo} - Clase {self.orden}: {self.titulo}"

class Suscripcion(models.Model):
    """El candado principal: Define qué usuario tiene acceso a qué curso"""
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='suscripciones')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='suscritos')
    fecha_compra = models.DateTimeField(auto_now_add=True)
    acceso_activo = models.BooleanField(default=True, help_text="Desmarcar si el alumno pide reembolso o incumple normas")

    class Meta:
        unique_together = ('usuario', 'curso') # Un alumno no puede comprar el mismo curso dos veces

    def __str__(self):
        return f"{self.usuario.username} -> {self.curso.titulo}"

class TransaccionPago(models.Model):
    """Registro contable para auditoría de pagos"""
    METODOS_PAGO = (
        ('ZELLE', 'Zelle'),
        ('PAGO_MOVIL', 'Pago Móvil'),
        ('EFECTIVO', 'Efectivo'),
        ('TRANSFERENCIA', 'Transferencia Bancaria'),
    )
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo = models.CharField(max_length=20, choices=METODOS_PAGO)
    referencia = models.CharField(max_length=100, unique=True)
    fecha_pago = models.DateTimeField(auto_now_add=True)
    verificado = models.BooleanField(default=False, help_text="Marcar manual/automáticamente cuando el dinero esté confirmado")

    def __str__(self):
        return f"Ref: {self.referencia} - {self.metodo} ({self.monto})"

class ProgresoClase(models.Model):
    """Seguimiento de la experiencia de usuario (Saber si ya vio el video)"""
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE)
    completada = models.BooleanField(default=False)
    fecha_completada = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('usuario', 'clase')

    def __str__(self):
        estado = "Completada" if self.completada else "Pendiente"
        return f"{self.usuario.username} - {self.clase.titulo}: {estado}"