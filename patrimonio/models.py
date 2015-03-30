# -*- encoding: UTF-8 -*-

#
#    Copyright 2013-2015
#
#      Rayco Abad-Martín <rayco.abad@gmail.com>
#      http://www.linkedin.com/in/rabad
#
#    This file is part of patrimonioULL.
#
#    patrimonioULL is free software: you can redistribute it and/or
#    modify it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    patrimonioULL is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with patrimonioULL.  If not, see
#    <http://www.gnu.org/licenses/>.
#

from .helpers import name_front, name_back, imagen_max_size
from django.conf import settings as st
from django.db import models
from tinymce import models as tinymce_models


class DisciplinaArtistica(models.Model):
    disciplina = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return u'%s' % self.disciplina

    class Meta:
        ordering = ['disciplina', ]
        verbose_name_plural = "Disciplinas Artísticas"


class LocalizacionObra(models.Model):
    codigo = models.CharField(
        u"Código de Registro", max_length=10, unique=True)

    localizacion = models.CharField(u"Localización", max_length=255)

    def __unicode__(self):
        return u'%s' % self.localizacion

    class Meta:
        ordering = ['localizacion', ]
        verbose_name_plural = "Localizaciones"


class FichaInventario(models.Model):
    registro = models.CharField(
        u"Nº Registro", max_length=50, unique=True)

    titulo = models.CharField(u"Título", max_length=255, blank=True)

    autor = models.CharField(max_length=50, blank=True)

    medidas = models.CharField(max_length=100, blank=True)

    tematica = models.CharField(
        u"Temática y Estilo", max_length=50, blank=True)

    tecnica = models.CharField(u"Técnica", max_length=50, blank=True)

    fecha = models.CharField(u"Fecha de Ejecución", max_length=100, blank=True)

    estado = models.CharField(
        choices=st.TIPOS_ESTADO, max_length=50, blank=True)

    desperfectos = tinymce_models.HTMLField(blank=True)

    ubicacion = tinymce_models.HTMLField(u"Ubicación", blank=True)

    contacto = tinymce_models.HTMLField(blank=True)

    observaciones = tinymce_models.HTMLField(blank=True)

    def __unicode__(self):
        return u'%s' % self.registro

    class Meta:
        abstract = True


class ObraDeArte(FichaInventario):

    imagen = models.ImageField(upload_to=name_front, blank=True)

    imagen_trasera = models.ImageField(upload_to=name_back, blank=True)

    disciplina = models.ForeignKey(
        'DisciplinaArtistica', on_delete=models.PROTECT)

    localizacion = models.ForeignKey(
        'LocalizacionObra', on_delete=models.PROTECT)

    def imagen_thumb(self):
        if self.imagen:
            thumb_width, thumb_height = imagen_max_size(
                self.imagen, st.MAX_THUMB_SIZE)
            return (u'<a href="%s%s" target="_blank"> \
                    <img src="%s%s" width="%s" height="%s" /></a>' %
                    (st.MEDIA_URL, self.imagen, st.MEDIA_URL,
                     self.imagen, thumb_width, thumb_height))
        return u''
    imagen_thumb.allow_tags = True
    imagen_thumb.short_description = u'Imagen'

    class Meta:
        verbose_name_plural = "Obras de Arte"


class Fotografia(FichaInventario):

    is_selected = models.NullBooleanField(u'Seleccionada')

    is_series = models.BooleanField(u'Serie de Fotografías', default=False)


class Image(models.Model):
    ficha_inventario = models.ForeignKey(Fotografia)
    imagen = models.ImageField(u'Imagen')

    class Meta:
        verbose_name_plural = u"Imágenes"
