# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models
import patrimonio.helpers


class Migration(migrations.Migration):

    dependencies = [
        ('patrimonio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fotografia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('registro', models.CharField(unique=True, max_length=50, verbose_name='N\xba Registro')),
                ('titulo', models.CharField(max_length=255, verbose_name='T\xedtulo', blank=True)),
                ('autor', models.CharField(max_length=50, blank=True)),
                ('medidas', models.CharField(max_length=100, blank=True)),
                ('tematica', models.CharField(max_length=50, verbose_name='Tem\xe1tica y Estilo', blank=True)),
                ('tecnica', models.CharField(max_length=50, verbose_name='T\xe9cnica', blank=True)),
                ('fecha', models.CharField(max_length=100, verbose_name='Fecha de Ejecuci\xf3n', blank=True)),
                ('estado', models.CharField(blank=True, max_length=50, choices=[(b'Bueno', b'Bueno'), (b'Malo', b'Malo'), (b'Regular', b'Regular')])),
                ('desperfectos', tinymce.models.HTMLField(blank=True)),
                ('ubicacion', tinymce.models.HTMLField(verbose_name='Ubicaci\xf3n', blank=True)),
                ('contacto', tinymce.models.HTMLField(blank=True)),
                ('observaciones', tinymce.models.HTMLField(blank=True)),
                ('is_selected', models.NullBooleanField(verbose_name='Seleccionada')),
                ('is_series', models.BooleanField(default=False, verbose_name='Serie de Fotograf\xedas')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imagen', models.ImageField(upload_to=patrimonio.helpers.image_path, verbose_name='Imagen')),
                ('ficha_inventario', models.ForeignKey(to='patrimonio.Fotografia')),
            ],
            options={
                'verbose_name_plural': 'Im\xe1genes',
            },
            bases=(models.Model,),
        ),
    ]
