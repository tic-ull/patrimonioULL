# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ObraDeArteNEW'
        db.create_table(u'patrimonio_obradeartenew', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('registro', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('autor', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('disciplina', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patrimonio.DisciplinaArtisticaNEW'], on_delete=models.PROTECT)),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('imagen_trasera', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('medidas', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('tematica', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('tecnica', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('fecha', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('localizacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patrimonio.LocalizacionObraNEW'], on_delete=models.PROTECT)),
            ('ubicacion', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('estado', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('desperfectos', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('contacto', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('observaciones', self.gf('tinymce.models.HTMLField')(blank=True)),
        ))
        db.send_create_signal(u'patrimonio', ['ObraDeArteNEW'])


    def backwards(self, orm):
        # Deleting model 'ObraDeArteNEW'
        db.delete_table(u'patrimonio_obradeartenew')


    models = {
        u'patrimonio.disciplinaartistica': {
            'Meta': {'ordering': "['disciplina']", 'object_name': 'DisciplinaArtistica'},
            'disciplina': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'})
        },
        u'patrimonio.disciplinaartisticanew': {
            'Meta': {'ordering': "['disciplina']", 'object_name': 'DisciplinaArtisticaNEW'},
            'disciplina': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'patrimonio.localizacionobra': {
            'Meta': {'ordering': "['localizacion']", 'object_name': 'LocalizacionObra'},
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '10', 'primary_key': 'True'}),
            'localizacion': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'patrimonio.localizacionobranew': {
            'Meta': {'ordering': "['localizacion']", 'object_name': 'LocalizacionObraNEW'},
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
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'imagen_trasera': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'localizacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patrimonio.LocalizacionObra']", 'on_delete': 'models.PROTECT'}),
            'medidas': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'observaciones': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'registro': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'tecnica': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'tematica': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'ubicacion': ('tinymce.models.HTMLField', [], {'blank': 'True'})
        },
        u'patrimonio.obradeartenew': {
            'Meta': {'object_name': 'ObraDeArteNEW'},
            'autor': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'contacto': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'desperfectos': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'disciplina': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patrimonio.DisciplinaArtisticaNEW']", 'on_delete': 'models.PROTECT'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'imagen_trasera': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'localizacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patrimonio.LocalizacionObraNEW']", 'on_delete': 'models.PROTECT'}),
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
