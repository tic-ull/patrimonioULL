# -*- coding: UTF-8 -*-

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

from django.conf import settings as st
from django.db import models
from tinymce import models as tinymce_models

import os


class DisciplinaArtistica(models.Model):
    disciplina = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return u'%s' % (self.disciplina)

    class Meta:
        ordering = ['disciplina', ]
        verbose_name_plural = "Disciplinas Artísticas"


class LocalizacionObra(models.Model):
    codigo = models.CharField(u"Código de Registro", max_length=10,
                              unique=True)
    localizacion = models.CharField(u"Localización", max_length=255)

    def __unicode__(self):
        return u'%s' % (self.localizacion)

    class Meta:
        ordering = ['localizacion', ]
        verbose_name_plural = "Localizaciones"


def content_file_name(instance, filename, side):
    extension = os.path.splitext(filename)[1]
    path = 'patrimonio/images/%s/%s_%s%s' % (instance.disciplina_id,
                                             instance.pk,
                                             side, extension)
    # Deleting the previous file, it doesn't rename with _number
    fullpath = os.path.join(st.MEDIA_ROOT, path)
    if os.path.exists(fullpath):
        os.remove(fullpath)
    return path


def name_front(instance, filename):
    return content_file_name(instance, filename, 'front')


def name_back(instance, filename):
    return content_file_name(instance, filename, 'back')


class ObraDeArte(models.Model):
    registro = models.CharField(u"Nº Registro", max_length=50,
                                unique=True)
    titulo = models.CharField(u"Título", max_length=255, blank=True)
    autor = models.CharField(max_length=50, blank=True)
    disciplina = models.ForeignKey('DisciplinaArtistica',
                                   on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to=name_front, blank=True)
    imagen_trasera = models.ImageField(upload_to=name_back, blank=True)
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
