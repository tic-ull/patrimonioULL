# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DisciplinaArtistica'
        db.create_table(u'patrimonio_disciplinaartistica', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('disciplina', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'patrimonio', ['DisciplinaArtistica'])

        # Adding model 'LocalizacionObra'
        db.create_table(u'patrimonio_localizacionobra', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('codigo', self.gf('django.db.models.fields.CharField')(unique=True, max_length=10)),
            ('localizacion', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'patrimonio', ['LocalizacionObra'])

        # Adding model 'ObraDeArte'
        db.create_table(u'patrimonio_obradearte', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('registro', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('autor', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('disciplina', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patrimonio.DisciplinaArtistica'], on_delete=models.PROTECT)),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('imagen_trasera', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('medidas', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('tematica', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('tecnica', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('fecha', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('localizacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patrimonio.LocalizacionObra'], on_delete=models.PROTECT)),
            ('ubicacion', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('estado', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('desperfectos', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('contacto', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('observaciones', self.gf('tinymce.models.HTMLField')(blank=True)),
        ))
        db.send_create_signal(u'patrimonio', ['ObraDeArte'])


    def backwards(self, orm):
        # Deleting model 'DisciplinaArtistica'
        db.delete_table(u'patrimonio_disciplinaartistica')

        # Deleting model 'LocalizacionObra'
        db.delete_table(u'patrimonio_localizacionobra')

        # Deleting model 'ObraDeArte'
        db.delete_table(u'patrimonio_obradearte')


    models = {
        u'patrimonio.disciplinaartistica': {
            'Meta': {'ordering': "['disciplina']", 'object_name': 'DisciplinaArtistica'},
            'disciplina': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'patrimonio.localizacionobra': {
            'Meta': {'ordering': "['localizacion']", 'object_name': 'LocalizacionObra'},
            'codigo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'localizacion': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'patrimonio.obradearte': {
            'Meta': {'object_name': 'ObraDeArte'},
            'autor': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'contacto': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'desperfectos': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'disciplina': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patrimonio.DisciplinaArtistica']", 'on_delete': 'models.PROTECT'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'imagen_trasera': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'localizacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patrimonio.LocalizacionObra']", 'on_delete': 'models.PROTECT'}),
            'medidas': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'observaciones': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'registro': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'tecnica': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'tematica': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'ubicacion': ('tinymce.models.HTMLField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['patrimonio']