from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _
from ckeditor.fields import RichTextField


class XperifunUser(AbstractUser):

    def __str__(self):
        return self.username

class Comunidad(models.Model):
    name = models.CharField(max_length=100, null=False, blank=True, verbose_name=_('Nombre de la comunidad autóma'))
    pagina_oficial = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('Pagina oficial del sitio'))
    latitude = models.CharField(max_length=255, null=False, blank=True, verbose_name=_('Latitude'))
    longitude = models.CharField(max_length=255, null=False, blank=True, verbose_name=_('Longitude'))
    scrapped_url = models.CharField(max_length=255, null=False, blank=True, default="", verbose_name=_('Scrapped url'))
    
class Provincia(models.Model):
    name = models.CharField(max_length=100, null=False, blank=True, verbose_name=_('Nombre de la provincia'))
    comunidad = models.ForeignKey(
        'provinces.Comunidad', verbose_name=_('Comunidad autónoma a la que pertenece'), on_delete=models.PROTECT,
        null=False, blank=False, help_text=_('Comunidad autónoma a la que pertenece',)
    )
    pagina_oficial = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('Pagina oficial del sitio'))
    latitude = models.CharField(max_length=255, null=False, blank=True, verbose_name=_('Latitude'))
    longitude = models.CharField(max_length=255, null=False, blank=True, verbose_name=_('Longitude'))
    scrapped_url = models.CharField(max_length=255, null=False, blank=True, default="", verbose_name=_('Scrapped url'))

class Municipio(models.Model):
    name = models.CharField(max_length=100, null=False, blank=True, verbose_name=_('Nombre del municipio'))
    provincia = models.ForeignKey(
        'provinces.Provincia', verbose_name=_('Provincia a la que pertenece'), on_delete=models.PROTECT,
        null=False, blank=False, help_text=_('Provincia a la que pertenece',)
    )
    num_habitantes = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('Pagina oficial del sitio'))
    pagina_oficial = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('Pagina oficial del sitio'))
    latitude = models.CharField(max_length=255, null=False, blank=True, verbose_name=_('Latitude'))
    longitude = models.CharField(max_length=255, null=False, blank=True, verbose_name=_('Longitude'))
    scrapped_url = models.CharField(max_length=255, null=False, blank=True, default="", verbose_name=_('Scrapped url'))

class Festivo(models.Model):
    municipio = models.ForeignKey(
        'provinces.Municipio', verbose_name=_('Municipio a la que pertenece'), on_delete=models.PROTECT,
        null=False, blank=False, help_text=_('Municipio a la que pertenece',)
    )
    name = models.CharField(max_length=100, null=False, blank=True, verbose_name="Nombre del festivo")
    fecha_inicio = models.DateField(null=False, blank=False)
    fecha_fin = models.DateField(null=True, blank=True)
    ciudad_cercana = models.CharField(max_length=255, null=True, blank=True, verbose_name="Ciudad relacionada")
    distancia = models.CharField(max_length=255, null=True, blank=True, verbose_name="Distancia")


