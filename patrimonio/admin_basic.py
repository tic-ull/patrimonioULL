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

from .admin_advanced import ObraAdmin, FotografiaAdmin, ImageInline
from .models import ObraDeArte, Fotografia
from core.admin_basic import basic_admin_site
from django import forms
from django.forms.util import flatatt
from django.utils.encoding import force_text
from django.utils.html import format_html
from django.utils.safestring import mark_safe


class ReadonlyTextArea(forms.Textarea):

    def render(self, name, value, attrs=None):
        attrs['style'] = 'display:none'
        final_attrs = self.build_attrs(attrs, name=name)
        return format_html(u'<textarea{0}>{1}</textarea><div>{2}</div>'.format(
            flatatt(final_attrs),
            force_text(value),
            mark_safe(value)
        ))


class ObraBasicAdmin(ObraAdmin):

    readonly_fields = (
        'registro', 'titulo', 'autor', 'fecha', 'medidas', 'tematica',
        'tecnica', 'disciplina', 'estado', 'localizacion',
        'imagen', 'imagen_trasera')

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in (
                'desperfectos', 'ubicacion', 'contacto', 'observaciones'):
            kwargs['widget'] = ReadonlyTextArea()
        return super(ObraBasicAdmin, self).formfield_for_dbfield(
            db_field, **kwargs)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context.update({
            'show_save_and_continue': False,
            'show_save': False,
        })
        return super(ObraBasicAdmin, self).change_view(
            request, object_id, form_url, extra_context=extra_context)

    def get_actions(self, request):
        """ Remove action delete object from list of actions """
        actions = super(ObraBasicAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


class ReadonlyImageInline(ImageInline):
    readonly_fields = ('imagen', )


class FotografiaBasicAdmin(FotografiaAdmin):

    readonly_fields = (
        'registro', 'titulo', 'autor', 'fecha', 'medidas', 'tematica',
        'tecnica', 'estado', 'is_series', 'is_selected')

    inlines = [
        ReadonlyImageInline,
    ]

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in (
                'desperfectos', 'ubicacion', 'contacto', 'observaciones'):
            kwargs['widget'] = ReadonlyTextArea()
        return super(FotografiaBasicAdmin, self).formfield_for_dbfield(
            db_field, **kwargs)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context.update({
            'show_save_and_continue': False,
            'show_save': False,
        })
        return super(FotografiaBasicAdmin, self).change_view(
            request, object_id, form_url, extra_context=extra_context)

    def get_actions(self, request):
        """ Remove action delete object from list of actions """
        actions = super(FotografiaBasicAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

basic_admin_site.register(ObraDeArte, ObraBasicAdmin)
basic_admin_site.register(Fotografia, FotografiaBasicAdmin)
