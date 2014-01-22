# -*- coding: UTF-8 -*-

from django.conf import settings as st
from django.db import models
from tinymce import models as tinymce_models


class DisciplinaArtistica(models.Model):
    disciplina = models.CharField(max_length=50, primary_key=True)

    def __unicode__(self):
        return u'%s' % (self.disciplina)

    class Meta:
        ordering = ['disciplina', ]
        verbose_name_plural = "Disciplinas Artísticas"


class LocalizacionObra(models.Model):
    codigo = models.CharField(u"Código de Registro", max_length=10,
                              primary_key=True)
    localizacion = models.CharField(u"Localización", max_length=255)

    def __unicode__(self):
        return u'%s' % (self.localizacion)

    class Meta:
        ordering = ['localizacion', ]
        verbose_name_plural = "Localizaciones"


class ObraDeArte(models.Model):
    registro = models.CharField(u"Nº Registro", max_length=50,
                                primary_key=True)
    titulo = models.CharField(u"Título", max_length=255, blank=True)
    autor = models.CharField(max_length=50, blank=True)
    disciplina = models.ForeignKey('DisciplinaArtistica',
                                   on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to='images', blank=True)
    imagen_trasera = models.ImageField(upload_to='images', blank=True)
    medidas = models.CharField(max_length=100, blank=True)
    tematica = models.CharField(u"Temática y Estilo", max_length=50,
                                blank=True)
    tecnica = models.CharField(u"Técnica", max_length=50, blank=True)
    fecha = models.CharField(u"Fecha de Ejecución", max_length=100, blank=True)
    localizacion = models.ForeignKey('LocalizacionObra',
                                     on_delete=models.PROTECT)
    ubicacion = tinymce_models.HTMLField(u"Ubicación", blank=True)
    estado = models.CharField(choices=st.TIPOS_ESTADO, max_length=50, blank=True)
    desperfectos = tinymce_models.HTMLField(blank=True)
    contacto = tinymce_models.HTMLField(blank=True)
    observaciones = tinymce_models.HTMLField(blank=True)

    def __unicode__(self):
        return u'%s' % (self.registro)

    def imagen_thumb(self):
        if self.imagen:
            max_imagen_size = max(self.imagen.width, self.imagen.height)
            ratio = (max_imagen_size > st.MAX_THUMB_SIZE and
                     float(max_imagen_size) / st.MAX_THUMB_SIZE or 1)
            thumb_width = self.imagen.width / ratio
            thumb_height = self.imagen.height / ratio
            return (u'<a href="%s%s" target="_blank"> \
                    <img src="%s%s" width="%s" height="%s" /></a>' %
                    (st.MEDIA_URL, self.imagen, st.MEDIA_URL,
                     self.imagen, thumb_width, thumb_height))
        return u''
    imagen_thumb.allow_tags = True
    imagen_thumb.short_description = u'Imagen'

    class Meta:
        verbose_name_plural = "Obras de Arte"
