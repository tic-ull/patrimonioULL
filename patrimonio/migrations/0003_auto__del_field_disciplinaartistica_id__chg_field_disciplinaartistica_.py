# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'DisciplinaArtistica.id'
        db.delete_column(u'patrimonio_disciplinaartistica', 'Id')


        # Changing field 'DisciplinaArtistica.disciplina'
        db.alter_column(u'patrimonio_disciplinaartistica', 'disciplina', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True))
        # Adding unique constraint on 'DisciplinaArtistica', fields ['disciplina']
        db.create_unique(u'patrimonio_disciplinaartistica', ['disciplina'])


    def backwards(self, orm):
        # Removing unique constraint on 'DisciplinaArtistica', fields ['disciplina']
        db.delete_unique(u'patrimonio_disciplinaartistica', ['disciplina'])


        # User chose to not deal with backwards NULL issues for 'DisciplinaArtistica.id'
        raise RuntimeError("Cannot reverse this migration. 'DisciplinaArtistica.id' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'DisciplinaArtistica.id'
        db.add_column(u'patrimonio_disciplinaartistica', 'id',
                      self.gf('django.db.models.fields.AutoField')(primary_key=True, db_column='Id'),
                      keep_default=False)


        # Changing field 'DisciplinaArtistica.disciplina'
        db.alter_column(u'patrimonio_disciplinaartistica', 'disciplina', self.gf('django.db.models.fields.CharField')(max_length=50))

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
            'escultura': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'estado_de_conservacion': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'fotografia': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'grabado': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "'Id'"}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'litografia': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'medidas': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'n_de_registro': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'observaciones': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'otros': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'pintura': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'tecnica': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'tematica_y_estilo': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'ubicacion': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['patrimonio']