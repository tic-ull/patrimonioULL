# -*- coding: UTF-8 -*-

from django.conf import settings as st
from django.contrib import admin
from django.utils.safestring import mark_safe
from patrimonio.models import (DisciplinaArtistica,
                               LocalizacionObra,
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


class DisciplinaFilter(admin.SimpleListFilter):
    title = 'Disciplina'
    parameter_name = 'disciplina'

    def lookups(self, request, model_admin):
        disciplinas = model_admin.queryset(request).values_list(
            'disciplina', flat=True
        ).distinct().order_by('disciplina')
        return [(disciplina, disciplina) for disciplina in disciplinas]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(disciplina__pk__exact=self.value())
        else:
            return queryset


class LocalizacionFilter(admin.SimpleListFilter):
    title = 'Localización'
    parameter_name = 'localizacion'

    def lookups(self, request, model_admin):
        localizaciones = model_admin.queryset(request).values_list(
            'localizacion', flat=True
        ).distinct().order_by('localizacion')
        return [(loc, LocalizacionObra.objects.filter(
            codigo__iexact=loc)[0]) for loc in localizaciones]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(localizacion__pk__exact=self.value())
        else:
            return queryset


# Register your models here.


class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('disciplina',)


class LocalizacionAdmin(admin.ModelAdmin):
    list_display = ('localizacion', 'codigo')


class ObraAdmin(admin.ModelAdmin):
    list_per_page = 20
    ordering = ('registro',)
    list_display = ('registro', 'titulo', 'imagen_thumb')
    search_fields = ('registro', 'titulo', 'autor', 'fecha')
    list_filter = (DisciplinaFilter, LocalizacionFilter,)
    fieldsets = (
        (None, {
            'classes': ('wide', 'extrapretty', ),
            'fields': (('registro', 'imagen'), ('titulo', 'autor'),
                       ('fecha', 'medidas'), ('tematica', 'tecnica'),
                       ('disciplina'))
        }),
        (u'Estado', {
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
        if db_field.name == 'imagen':
            kwargs.pop("request", None)
            kwargs['widget'] = AdminImageWidget
            return db_field.formfield(**kwargs)
        return super(ObraAdmin,
                     self).formfield_for_dbfield(db_field, **kwargs)

admin.site.register(DisciplinaArtistica, DisciplinaAdmin)
admin.site.register(LocalizacionObra, LocalizacionAdmin)
admin.site.register(ObraDeArte, ObraAdmin)
