# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ObraDeArte.otros'
        db.delete_column(u'patrimonio_obradearte', 'otros')

        # Deleting field 'ObraDeArte.pintura'
        db.delete_column(u'patrimonio_obradearte', 'pintura')

        # Deleting field 'ObraDeArte.ceramica'
        db.delete_column(u'patrimonio_obradearte', 'ceramica')

        # Deleting field 'ObraDeArte.escultura'
        db.delete_column(u'patrimonio_obradearte', 'escultura')

        # Deleting field 'ObraDeArte.fotografia'
        db.delete_column(u'patrimonio_obradearte', 'fotografia')

        # Deleting field 'ObraDeArte.dibujo'
        db.delete_column(u'patrimonio_obradearte', 'dibujo')

        # Deleting field 'ObraDeArte.litografia'
        db.delete_column(u'patrimonio_obradearte', 'litografia')

        # Deleting field 'ObraDeArte.grabado'
        db.delete_column(u'patrimonio_obradearte', 'grabado')


    def backwards(self, orm):
        # Adding field 'ObraDeArte.otros'
        db.add_column(u'patrimonio_obradearte', 'otros',
                      self.gf('django.db.models.fields.NullBooleanField')(default=False, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ObraDeArte.pintura'
        db.add_column(u'patrimonio_obradearte', 'pintura',
                      self.gf('django.db.models.fields.NullBooleanField')(default=False, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ObraDeArte.ceramica'
        db.add_column(u'patrimonio_obradearte', 'ceramica',
                      self.gf('django.db.models.fields.NullBooleanField')(default=False, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ObraDeArte.escultura'
        db.add_column(u'patrimonio_obradearte', 'escultura',
                      self.gf('django.db.models.fields.NullBooleanField')(default=False, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ObraDeArte.fotografia'
        db.add_column(u'patrimonio_obradearte', 'fotografia',
                      self.gf('django.db.models.fields.NullBooleanField')(default=False, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ObraDeArte.dibujo'
        db.add_column(u'patrimonio_obradearte', 'dibujo',
                      self.gf('django.db.models.fields.NullBooleanField')(default=False, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ObraDeArte.litografia'
        db.add_column(u'patrimonio_obradearte', 'litografia',
                      self.gf('django.db.models.fields.NullBooleanField')(default=False, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ObraDeArte.grabado'
        db.add_column(u'patrimonio_obradearte', 'grabado',
                      self.gf('django.db.models.fields.NullBooleanField')(default=False, null=True, blank=True),
                      keep_default=False)


    models = {
        u'patrimonio.disciplinaartistica': {
            'Meta': {'object_name': 'DisciplinaArtistica'},
            'disciplina': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'})
        },
        u'patrimonio.obradearte': {
            'Meta': {'object_name': 'ObraDeArte'},
            'autor': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'contacto': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'desperfectos': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'disciplina': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patrimonio.DisciplinaArtistica']", 'on_delete': 'models.PROTECT'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'medidas': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'observaciones': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'registro': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'tecnica': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'tematica': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'ubicacion': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['patrimonio']