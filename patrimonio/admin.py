# -*- coding: UTF-8 -*-

from django.conf import settings as st
from django.contrib import admin
from django.utils.safestring import mark_safe
from patrimonio.models import (DisciplinaArtistica,
                               ObraDeArte)


class AdminImageWidget(admin.widgets.AdminFileWidget):
    def render(self, name, imagen, attrs=None):
        output = []
        if imagen and getattr(imagen, "url", None):
            max_imagen_size = max(imagen.width, imagen.height)
            ratio = (max_imagen_size > st.MAX_IMAGEN_SIZE and
                     float(max_imagen_size) / st.MAX_IMAGEN_SIZE or 1)
            width = imagen.width / ratio
            height = imagen.height / ratio
            output.append(u'<a href="%s" target="_blank"> \
                          <img src="%s" width="%s height="%s"/></a>' %
                          (imagen.url, imagen.url, width, height))
        output.append(super(admin.widgets.AdminFileWidget,
                            self).render(name, imagen, attrs))
        return mark_safe(u''.join(output))

# Register your models here.


class DisciplinaAdmin(admin.ModelAdmin):
    ordering = ('disciplina',)
    list_display = ('disciplina',)


class ObraAdmin(admin.ModelAdmin):
    list_per_page = 20
    ordering = ('n_de_registro',)
    list_display = ('n_de_registro', 'titulo', 'imagen_thumb')
    search_fields = ('n_de_registro', 'titulo', 'autor', 'fecha')
    fieldsets = (
        (None, {
            'classes': ('wide', 'extrapretty', ),
            'fields': (('n_de_registro', 'imagen'), ('titulo', 'autor'),
                       ('fecha', 'medidas'), ('tematica_y_estilo', 'tecnica'))
        }),
        (u'Disciplinas Artísticas', {
            'fields': (('dibujo', 'pintura', 'escultura', 'fotografia'),
                       ('grabado', 'ceramica', 'litografia', 'otros'))
        }),
        (u'Estado', {
            'classes': ('wide', 'extrapretty', ),
            'fields': ('estado_de_conservacion', 'desperfectos')
        }),
        (None, {
            'classes': ('wide', 'extrapretty', ),
            'fields': (('ubicacion', 'contacto'), 'observaciones')
        }),
    )

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'imagen':
            kwargs.pop("request", None)
            kwargs['widget'] = AdminImageWidget
            return db_field.formfield(**kwargs)
        return super(ObraAdmin,
                     self).formfield_for_dbfield(db_field, **kwargs)

admin.site.register(DisciplinaArtistica, DisciplinaAdmin)
admin.site.register(ObraDeArte, ObraAdmin)
