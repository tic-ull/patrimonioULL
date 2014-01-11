# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ObraDeArte.disciplina'
        db.add_column(u'patrimonio_obradearte', 'disciplina',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='CERAMICA', to=orm['patrimonio.DisciplinaArtistica'], on_delete=models.PROTECT),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ObraDeArte.disciplina'
        db.delete_column(u'patrimonio_obradearte', 'disciplina_id')


    models = {
        u'patrimonio.disciplinaartistica': {
            'Meta': {'object_name': 'DisciplinaArtistica'},
            'disciplina': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'})
        },
        u'patrimonio.obradearte': {
            'Meta': {'object_name': 'ObraDeArte'},
            'autor': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'ceramica': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'contacto': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'desperfectos': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'dibujo': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'disciplina': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patrimonio.DisciplinaArtistica']", 'on_delete': 'models.PROTECT'}),
            'escultura': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'fotografia': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'grabado': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'litografia': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'medidas': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'observaciones': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'otros': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'pintura': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'registro': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'tecnica': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'tematica': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'ubicacion': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['patrimonio']