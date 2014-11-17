# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import tinymce.models
import patrimonio.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DisciplinaArtistica',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('disciplina', models.CharField(unique=True, max_length=50)),
            ],
            options={
                'ordering': ['disciplina'],
                'verbose_name_plural': 'Disciplinas Art\xedsticas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LocalizacionObra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(unique=True, max_length=10, verbose_name='C\xf3digo de Registro')),
                ('localizacion', models.CharField(max_length=255, verbose_name='Localizaci\xf3n')),
            ],
            options={
                'ordering': ['localizacion'],
                'verbose_name_plural': 'Localizaciones',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ObraDeArte',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('registro', models.CharField(unique=True, max_length=50, verbose_name='N\xba Registro')),
                ('titulo', models.CharField(max_length=255, verbose_name='T\xedtulo', blank=True)),
                ('autor', models.CharField(max_length=50, blank=True)),
                ('imagen', models.ImageField(upload_to=patrimonio.models.name_front, blank=True)),
                ('imagen_trasera', models.ImageField(upload_to=patrimonio.models.name_back, blank=True)),
                ('medidas', models.CharField(max_length=100, blank=True)),
                ('tematica', models.CharField(max_length=50, verbose_name='Tem\xe1tica y Estilo', blank=True)),
                ('tecnica', models.CharField(max_length=50, verbose_name='T\xe9cnica', blank=True)),
                ('fecha', models.CharField(max_length=100, verbose_name='Fecha de Ejecuci\xf3n', blank=True)),
                ('ubicacion', tinymce.models.HTMLField(verbose_name='Ubicaci\xf3n', blank=True)),
                ('estado', models.CharField(blank=True, max_length=50, choices=[(b'Bueno', b'Bueno'), (b'Malo', b'Malo'), (b'Regular', b'Regular')])),
                ('desperfectos', tinymce.models.HTMLField(blank=True)),
                ('contacto', tinymce.models.HTMLField(blank=True)),
                ('observaciones', tinymce.models.HTMLField(blank=True)),
                ('disciplina', models.ForeignKey(to='patrimonio.DisciplinaArtistica', on_delete=django.db.models.deletion.PROTECT)),
                ('localizacion', models.ForeignKey(to='patrimonio.LocalizacionObra', on_delete=django.db.models.deletion.PROTECT)),
            ],
            options={
                'verbose_name_plural': 'Obras de Arte',
            },
            bases=(models.Model,),
        ),
    ]
