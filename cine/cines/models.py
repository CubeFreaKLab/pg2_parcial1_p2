from django.db import models

class Director(models.Model):
    """
    Modelo para representar a un director de cine
    """
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Director"
        verbose_name_plural = "Directores"
        ordering = ['nombre']

class Pelicula(models.Model):
    """
    Modelo para representar una película
    """
    titulo = models.CharField(max_length=200)
    anio_estreno = models.IntegerField(verbose_name="Año de estreno")
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='peliculas')
    
    def __str__(self):
        return f"{self.titulo} ({self.anio_estreno})"
    
    class Meta:
        verbose_name = "Película"
        verbose_name_plural = "Películas"
        ordering = ['titulo']