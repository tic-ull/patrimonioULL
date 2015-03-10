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

from .helpers import imagen_max_size
from .models import (DisciplinaArtistica, LocalizacionObra, ObraDeArte,
                     Image, Fotografia)
from .obraPDF import ObraPDF
from django.conf import settings as st
from django.contrib import admin
from django.http import HttpResponse
from django.utils.safestring import mark_safe
from django_object_actions import DjangoObjectActions
from slugify import slugify


class AdminImageWidget(admin.widgets.AdminFileWidget):
    def render(self, name, imagen, attrs=None):
        output = []
        if imagen and getattr(imagen, "url", None):
            width, height = imagen_max_size(imagen, st.MAX_IMAGEN_SIZE)
            output.append(u'<a href="%s" target="_blank"> \
                          <img src="%s" width="%s height="%s"/></a>' %
                          (imagen.url, imagen.url, width, height))
        output.append(super(admin.widgets.AdminFileWidget,
                            self).render(name, imagen, attrs))
        return mark_safe(u''.join(output))


class DisciplinaFilter(admin.SimpleListFilter):
    title = 'Disciplina'
    parameter_name = 'disciplina'

    def lookups(self, request, model_admin):
        return DisciplinaArtistica.objects.values_list('pk', 'disciplina')

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(disciplina=self.value())
        else:
            return queryset


class LocalizacionFilter(admin.SimpleListFilter):
    title = 'Localización'
    parameter_name = 'localizacion'

    def lookups(self, request, model_admin):
        return LocalizacionObra.objects.values_list('pk', 'localizacion')

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(localizacion=self.value())
        else:
            return queryset


class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('disciplina',)


class LocalizacionAdmin(admin.ModelAdmin):
    list_display = ('localizacion', 'codigo')


class ObraAdmin(DjangoObjectActions, admin.ModelAdmin):
    list_per_page = 20
    ordering = ('registro',)
    list_display = ('registro', 'titulo', 'imagen_thumb')
    search_fields = ('registro', 'titulo', 'autor', 'fecha')
    list_filter = (DisciplinaFilter, LocalizacionFilter,)
    fieldsets = (
        (None, {
            'classes': ('extrapretty', ),
            'fields': ('registro', ('imagen', 'imagen_trasera'))
        }),
        (None, {
            'classes': ('wide', 'extrapretty', ),
            'fields': (('titulo', 'autor'), ('fecha', 'medidas'),
                       ('tematica', 'tecnica'), 'disciplina')
        }),
        (u'Estado de Conservación', {
            'classes': ('wide', 'extrapretty', ),
            'fields': ('estado', 'desperfectos')
        }),
        (None, {
            'classes': ('wide', 'extrapretty', ),
            'fields': ('localizacion', 'ubicacion',
                       'contacto', 'observaciones')
        }),
    )

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ('imagen', 'imagen_trasera'):
            kwargs.pop("request", None)
            kwargs['widget'] = AdminImageWidget
            return db_field.formfield(**kwargs)
        return super(ObraAdmin,
                     self).formfield_for_dbfield(db_field, **kwargs)

    def print_pdf(self, request, obj):
        response = HttpResponse(content_type='application/pdf')
        filename = slugify(
            unicode(obj.pk) + "-" + obj.titulo) + ".pdf"
        response['Content-Disposition'] = (
            'attachment;' 'filename="%s"' % filename)
        response.write(ObraPDF(obj).go())
        return response
    print_pdf.label = "Imprimir"
    print_pdf.short_description = "Imprimir en PDF"

    objectactions = ('print_pdf', )


class ImageInline(admin.StackedInline):
    model = Image
    extra = 0

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name is 'imagen':
            kwargs.pop("request", None)
            kwargs['widget'] = AdminImageWidget
            return db_field.formfield(**kwargs)
        return super(ImageInline,
                     self).formfield_for_dbfield(db_field, **kwargs)


class FotografiaAdmin(admin.ModelAdmin):
    list_per_page = 20
    ordering = ('registro',)
    list_display = ('registro', 'titulo',)
    search_fields = ('registro', 'titulo', 'autor', 'fecha',)

    inlines = [
        ImageInline,
    ]

    fieldsets = (
        (None, {
            'classes': ('extrapretty', ),
            'fields': ('registro',)
        }),
        (None, {
            'classes': ('wide', 'extrapretty', ),
            'fields': (('titulo', 'autor'), ('fecha', 'medidas'),
                       ('tematica', 'tecnica'))
        }),
        (u'Estado de Conservación', {
            'classes': ('wide', 'extrapretty', ),
            'fields': ('estado', 'desperfectos')
        }),
        (None, {
            'classes': ('wide', 'extrapretty', ),
            'fields': ('contacto', 'observaciones')
        }),
    )

admin.site.register(DisciplinaArtistica, DisciplinaAdmin)
admin.site.register(LocalizacionObra, LocalizacionAdmin)
admin.site.register(ObraDeArte, ObraAdmin)
admin.site.register(Fotografia, FotografiaAdmin)
