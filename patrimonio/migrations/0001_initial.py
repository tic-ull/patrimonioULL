# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DisciplinaArtistica'
        db.create_table(u'patrimonio_disciplinaartistica', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True, db_column='Id')),
            ('disciplina', self.gf('django.db.models.fields.CharField')(max_length=50, db_column='DISCIPLINAS ARTISTICAS', blank=True)),
        ))
        db.send_create_signal(u'patrimonio', ['DisciplinaArtistica'])

        # Adding model 'ObraDeArte'
        db.create_table(u'patrimonio_obradearte', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True, db_column='Id')),
            ('n_de_registro', self.gf('django.db.models.fields.CharField')(max_length=50, db_column='N DE REGISTRO', blank=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=255, db_column='TITULO', blank=True)),
            ('autor', self.gf('django.db.models.fields.CharField')(max_length=50, db_column='AUTOR', blank=True)),
            ('dibujo', self.gf('django.db.models.fields.NullBooleanField')(default=False, null=True, db_column='DIBUJO', blank=True)),
            ('pintura', self.gf('django.db.models.fields.NullBooleanField')(default=False, null=True, db_column='PINTURA', blank=True)),
            ('escultura', self.gf('django.db.models.fields.NullBooleanField')(default=False, null=True, db_column='ESCULTURA', blank=True)),
            ('fotografia', self.gf('django.db.models.fields.NullBooleanField')(default=False, null=True, db_column='FOTOGRAFIA', blank=True)),
            ('grabado', self.gf('django.db.models.fields.NullBooleanField')(default=False, null=True, db_column='GRABADO', blank=True)),
            ('ceramica', self.gf('django.db.models.fields.NullBooleanField')(default=False, null=True, db_column='CERAMICA', blank=True)),
            ('litografia', self.gf('django.db.models.fields.NullBooleanField')(default=False, null=True, db_column='LITOGRAFIA', blank=True)),
            ('otros', self.gf('django.db.models.fields.NullBooleanField')(default=False, null=True, db_column='OTROS', blank=True)),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100, db_column='IMAGEN', blank=True)),
            ('medidas', self.gf('django.db.models.fields.CharField')(max_length=100, db_column='MEDIDAS', blank=True)),
            ('tematica_y_estilo', self.gf('django.db.models.fields.CharField')(max_length=50, db_column='TEMATICA Y ESTILO', blank=True)),
            ('tecnica', self.gf('django.db.models.fields.CharField')(max_length=50, db_column='TECNICA', blank=True)),
            ('fecha', self.gf('django.db.models.fields.CharField')(max_length=100, db_column='FECHA', blank=True)),
            ('ubicacion', self.gf('django.db.models.fields.TextField')(db_column='UBICACION', blank=True)),
            ('estado_de_conservacion', self.gf('django.db.models.fields.CharField')(max_length=50, db_column='ESTADO DE CONSERVACION', blank=True)),
            ('desperfectos', self.gf('django.db.models.fields.TextField')(db_column='DESPERFECTOS', blank=True)),
            ('contacto', self.gf('django.db.models.fields.TextField')(db_column='CONTACTO', blank=True)),
            ('observaciones', self.gf('django.db.models.fields.TextField')(db_column='OBSERVACIONES', blank=True)),
        ))
        db.send_create_signal(u'patrimonio', ['ObraDeArte'])


    def backwards(self, orm):
        # Deleting model 'DisciplinaArtistica'
        db.delete_table(u'patrimonio_disciplinaartistica')

        # Deleting model 'ObraDeArte'
        db.delete_table(u'patrimonio_obradearte')


    models = {
        u'patrimonio.disciplinaartistica': {
            'Meta': {'object_name': 'DisciplinaArtistica'},
            'disciplina': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "'DISCIPLINAS ARTISTICAS'", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "'Id'"})
        },
        u'patrimonio.obradearte': {
            'Meta': {'object_name': 'ObraDeArte'},
            'autor': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "'AUTOR'", 'blank': 'True'}),
            'ceramica': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'db_column': "'CERAMICA'", 'blank': 'True'}),
            'contacto': ('django.db.models.fields.TextField', [], {'db_column': "'CONTACTO'", 'blank': 'True'}),
            'desperfectos': ('django.db.models.fields.TextField', [], {'db_column': "'DESPERFECTOS'", 'blank': 'True'}),
            'dibujo': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'db_column': "'DIBUJO'", 'blank': 'True'}),
            'escultura': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'db_column': "'ESCULTURA'", 'blank': 'True'}),
            'estado_de_conservacion': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "'ESTADO DE CONSERVACION'", 'blank': 'True'}),
            'fecha': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "'FECHA'", 'blank': 'True'}),
            'fotografia': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'db_column': "'FOTOGRAFIA'", 'blank': 'True'}),
            'grabado': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'db_column': "'GRABADO'", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "'Id'"}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'db_column': "'IMAGEN'", 'blank': 'True'}),
            'litografia': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'db_column': "'LITOGRAFIA'", 'blank': 'True'}),
            'medidas': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "'MEDIDAS'", 'blank': 'True'}),
            'n_de_registro': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "'N DE REGISTRO'", 'blank': 'True'}),
            'observaciones': ('django.db.models.fields.TextField', [], {'db_column': "'OBSERVACIONES'", 'blank': 'True'}),
            'otros': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'db_column': "'OTROS'", 'blank': 'True'}),
            'pintura': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'db_column': "'PINTURA'", 'blank': 'True'}),
            'tecnica': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "'TECNICA'", 'blank': 'True'}),
            'tematica_y_estilo': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "'TEMATICA Y ESTILO'", 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "'TITULO'", 'blank': 'True'}),
            'ubicacion': ('django.db.models.fields.TextField', [], {'db_column': "'UBICACION'", 'blank': 'True'})
        }
    }

    complete_apps = ['patrimonio']