# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ObraDeArte.localizacion'
        db.add_column(u'patrimonio_obradearte', 'localizacion',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='CA', to=orm['patrimonio.LocalizacionObra'], on_delete=models.PROTECT),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ObraDeArte.localizacion'
        db.delete_column(u'patrimonio_obradearte', 'localizacion_id')


    models = {
        u'patrimonio.disciplinaartistica': {
            'Meta': {'ordering': "['disciplina']", 'object_name': 'DisciplinaArtistica'},
            'disciplina': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'})
        },
        u'patrimonio.localizacionobra': {
            'Meta': {'ordering': "['localizacion']", 'object_name': 'LocalizacionObra'},
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '10', 'primary_key': 'True'}),
            'localizacion': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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
            'localizacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patrimonio.LocalizacionObra']", 'on_delete': 'models.PROTECT'}),
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
