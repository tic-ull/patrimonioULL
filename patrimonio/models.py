# -*- coding: UTF-8 -*-

from django.db import models
from django.conf import settings

class Disciplina(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    disciplina = models.CharField(db_column='DISCIPLINAS ARTISTICAS', max_length=50, blank=True)
    
    def __unicode__(self):
        return u'%s' % (self.disciplina)
    
    class Meta:
        managed = False
        db_table = 'AUXILIAR DISCIPLINAS ARTISTICAS'

class FichaDeInventario(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    n_de_registro = models.CharField(u"Nº de Registro", db_column='N DE REGISTRO', max_length=50, blank=True)
    titulo = models.CharField(u"Título", db_column='TITULO', max_length=255, blank=True)
    autor = models.CharField(db_column='AUTOR', max_length=50, blank=True)
    dibujo = models.NullBooleanField(db_column='DIBUJO', default=False)
    pintura = models.NullBooleanField(db_column='PINTURA', default=False)
    escultura = models.NullBooleanField(db_column='ESCULTURA', default=False)
    fotografia = models.NullBooleanField(db_column='FOTOGRAFIA', default=False)
    grabado = models.NullBooleanField(db_column='GRABADO', default=False)
    ceramica = models.NullBooleanField(db_column='CERAMICA', default=False)
    litografia = models.NullBooleanField(db_column='LITOGRAFIA', default=False)
    otros = models.NullBooleanField(db_column='OTROS', default=False)
    imagen = models.ImageField(db_column="IMAGEN", upload_to='images', blank=True)
    medidas = models.CharField(db_column='MEDIDAS', max_length=100, blank=True)
    tematica_y_estilo = models.CharField(u"Temática y Estilo", db_column='TEMATICA Y ESTILO', max_length=50, blank=True)
    tecnica = models.CharField(u"Técnica", db_column='TECNICA', max_length=50, blank=True)
    fecha = models.CharField(db_column='FECHA', max_length=100, blank=True)
    ubicacion = models.TextField(u"Ubicación", db_column='UBICACION', blank=True)
    estado_de_conservacion = models.CharField(u"Estado de Conservación", db_column='ESTADO DE CONSERVACION', max_length=50, blank=True)
    desperfectos = models.TextField(db_column='DESPERFECTOS', blank=True)
    contacto = models.TextField(db_column='CONTACTO', blank=True)
    observaciones = models.TextField(db_column='OBSERVACIONES', blank=True)
 
    def __unicode__(self):
        return u'%s' % (self.n_de_registro)

    def imagen_thumb(self):
        if self.imagen:
            max_imagen_size = max(self.imagen.width, self.imagen.height)
            ratio = max_imagen_size > settings.MAX_THUMB_SIZE and float(max_imagen_size) / settings.MAX_THUMB_SIZE or 1
            thumb_width = self.imagen.width / ratio
            thumb_height = self.imagen.height / ratio
            return (u'<a href="%s%s" target="_blank"><img src="%s%s" width="%s" height="%s" /></a>' % \
                (settings.MEDIA_URL, self.imagen, settings.MEDIA_URL, self.imagen, thumb_width, thumb_height))
        return u''
    imagen_thumb.allow_tags = True
    imagen_thumb.short_description = u'Imagen'

    class Meta:
        managed = False
        db_table = 'TABLA DE FICHAS DEL INVENTARIO'

