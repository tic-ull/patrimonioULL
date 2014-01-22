# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'DisciplinaArtistica.id'
        db.add_column(u'patrimonio_disciplinaartistica', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=0,primary_key=True),
                      keep_default=False)


        # Changing field 'DisciplinaArtistica.disciplina'
        db.alter_column(u'patrimonio_disciplinaartistica', 'disciplina', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50))

        # Changing field 'ObraDeArte.desperfectos'
        db.alter_column(u'patrimonio_obradearte', 'desperfectos', self.gf('tinymce.models.HTMLField')())

        # Changing field 'ObraDeArte.ubicacion'
        db.alter_column(u'patrimonio_obradearte', 'ubicacion', self.gf('tinymce.models.HTMLField')())

        # Changing field 'ObraDeArte.contacto'
        db.alter_column(u'patrimonio_obradearte', 'contacto', self.gf('tinymce.models.HTMLField')())

        # Changing field 'ObraDeArte.observaciones'
        db.alter_column(u'patrimonio_obradearte', 'observaciones', self.gf('tinymce.models.HTMLField')())

    def backwards(self, orm):
        # Deleting field 'DisciplinaArtistica.id'
        db.delete_column(u'patrimonio_disciplinaartistica', u'id')


        # Changing field 'DisciplinaArtistica.disciplina'
        db.alter_column(u'patrimonio_disciplinaartistica', 'disciplina', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True))

        # Changing field 'ObraDeArte.desperfectos'
        db.alter_column(u'patrimonio_obradearte', 'desperfectos', self.gf('django.db.models.fields.TextField')())

        # Changing field 'ObraDeArte.ubicacion'
        db.alter_column(u'patrimonio_obradearte', 'ubicacion', self.gf('django.db.models.fields.TextField')())

        # Changing field 'ObraDeArte.contacto'
        db.alter_column(u'patrimonio_obradearte', 'contacto', self.gf('django.db.models.fields.TextField')())

        # Changing field 'ObraDeArte.observaciones'
        db.alter_column(u'patrimonio_obradearte', 'observaciones', self.gf('django.db.models.fields.TextField')())

    models = {
        u'patrimonio.disciplinaartistica': {
            'Meta': {'ordering': "['disciplina']", 'object_name': 'DisciplinaArtistica'},
            'disciplina': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'patrimonio.localizacionobra': {
            'Meta': {'ordering': "['localizacion']", 'object_name': 'LocalizacionObra'},
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '10', 'primary_key': 'True'}),
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
        }
    }

    complete_apps = ['patrimonio']
