from django.db import models

# Create your models here.
class Explorer(models.Model):
    identi=models.CharField(max_length=200,verbose_name="Identificador",null=True, blank=True)
    title= models.CharField(max_length=200,verbose_name="Titulo")
    depart= models.CharField(max_length=100,verbose_name="Departamento")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen", upload_to="explorers")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated= models.DateTimeField(auto_now=True, verbose_name="Fecha de ediccion")
    class Meta:
        verbose_name="lugar"
        verbose_name_plural="lugares"
        ordering =["created"]
    def __str__(self) -> str:
        return self.title
 