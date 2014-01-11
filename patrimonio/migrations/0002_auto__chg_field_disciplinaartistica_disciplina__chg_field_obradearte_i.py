# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Renaming column for 'DisciplinaArtistica.disciplina' to match new field type.
        db.rename_column(u'patrimonio_disciplinaartistica', 'DISCIPLINAS ARTISTICAS', 'disciplina')
        # Changing field 'DisciplinaArtistica.disciplina'
        db.alter_column(u'patrimonio_disciplinaartistica', 'disciplina', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Renaming column for 'ObraDeArte.imagen' to match new field type.
        db.rename_column(u'patrimonio_obradearte', 'IMAGEN', 'imagen')
        # Changing field 'ObraDeArte.imagen'
        db.alter_column(u'patrimonio_obradearte', 'imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100))

        # Renaming column for 'ObraDeArte.otros' to match new field type.
        db.rename_column(u'patrimonio_obradearte', 'OTROS', 'otros')
        # Changing field 'ObraDeArte.otros'
        db.alter_column(u'patrimonio_obradearte', 'otros', self.gf('django.db.models.fields.NullBooleanField')(null=True))

        # Renaming column for 'ObraDeArte.pintura' to match new field type.
        db.rename_column(u'patrimonio_obradearte', 'PINTURA', 'pintura')
        # Changing field 'ObraDeArte.pintura'
        db.alter_column(u'patrimonio_obradearte', 'pintura', self.gf('django.db.models.fields.NullBooleanField')(null=True))

        # Renaming column for 'ObraDeArte.tematica_y_estilo' to match new field type.
        db.rename_column(u'patrimonio_obradearte', 'TEMATICA Y ESTILO', 'tematica_y_estilo')
        # Changing field 'ObraDeArte.tematica_y_estilo'
        db.alter_column(u'patrimonio_obradearte', 'tematica_y_estilo', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Renaming column for 'ObraDeArte.fecha' to match new field type.
        db.rename_column(u'patrimonio_obradearte', 'FECHA', 'fecha')
        # Changing field 'ObraDeArte.fecha'
        db.alter_column(u'patrimonio_obradearte', 'fecha', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Renaming column for 'ObraDeArte.n_de_registro' to match new field type.
        db.rename_column(u'patrimonio_obradearte', 'N DE REGISTRO', 'n_de_registro')
        # Changing field 'ObraDeArte.n_de_registro'
        db.alter_column(u'patrimonio_obradearte', 'n_de_registro', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Renaming column for 'ObraDeArte.ubicacion' to match new field type.
        db.rename_column(u'patrimonio_obradearte', 'UBICACION', 'ubicacion')
        # Changing field 'ObraDeArte.ubicacion'
        db.alter_column(u'patrimonio_obradearte', 'ubicacion', self.gf('django.db.models.fields.TextField')())

        # Renaming column for 'ObraDeArte.titulo' to match new field type.
        db.rename_column(u'patrimonio_obradearte', 'TITULO', 'titulo')
        # Changing field 'ObraDeArte.titulo'
        db.alter_column(u'patrimonio_obradearte', 'titulo', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Renaming column for 'ObraDeArte.contacto' to match new field type.
        db.rename_column(u'patrimonio_obradearte', 'CONTACTO', 'contacto')
        # Changing field 'ObraDeArte.contacto'
        db.alter_column(u'patrimonio_obradearte', 'contacto', self.gf('django.db.models.fields.TextField')())

        # Renaming column for 'ObraDeArte.observaciones' to match new field type.
        db.rename_column(u'patrimonio_obradearte', 'OBSERVACIONES', 'observaciones')
        # Changing field 'ObraDeArte.observaciones'
        db.alter_column(u'patrimonio_obradearte', 'observaciones', self.gf('django.db.models.fields.TextField')())

        # Renaming column for 'ObraDeArte.ceramica' to match new field type.
        db.rename_column(u'patrimonio_obradearte', 'CERAMICA', 'ceramica')
        # Changing field 'ObraDeArte.ceramica'
        db.alter_column(u'patrimonio_obradearte', 'ceramica', self.gf('django.db.models.fields.NullBooleanField')(null=True))

        # Renaming column for 'ObraDeArte.escultura' to match new field type.
        db.rename_column(u'patrimonio_obradearte', 'ESCULTURA', 'escultura')
        # Changing field 'ObraDeArte.escultura'
        db.alter_column(u'patrimonio_obradearte', 'escultura', self.gf('django.db.models.fields.NullBooleanField')(null=True))

        # Renaming column for 'ObraDeArte.autor' to match new field type.
        db.rename_column(u'patrimonio_obradearte', 'AUTOR', 'autor')
        # Changing field 'ObraDeArte.autor'
        db.alter_column(u'patrimonio_obradearte', 'autor', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Renaming column for 'ObraDeArte.fotografia' to match new field type.
        db.rename_column(u'patrimonio_obradearte', 'FOTOGRAFIA', 'fotografia')
        # Changing field 'ObraDeArte.fotografia'
        db.alter_column(u'patrimonio_obradearte', 'fotografia', self.gf('django.db.models.fields.NullBooleanField')(null=True))

        # Renaming column for 'ObraDeArte.dibujo' to match new field type.
        db.rename_column(u'patrimonio_obradearte', 'DIBUJO', 'dibujo')
        # Changing field 'ObraDeArte.dibujo'
        db.alter_column(u'patrimonio_obradearte', 'dibujo', self.gf('django.db.models.fields.NullBooleanField')(null=True))

        # Renaming column for 'ObraDeArte.tecnica' to match new field type.
        db.rename_column(u'patrimonio_obradearte', 'TECNICA', 'tecnica')
        # Changing field 'ObraDeArte.tecnica'
        db.alter_column(u'patrimonio_obradearte', 'tecnica', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Renaming column for 'ObraDeArte.litografia' to match new field type.
        db.rename_column(u'patrimonio_obradearte', 'LITOGRAFIA', 'litografia')
        # Changing field 'ObraDeArte.litografia'
        db.alter_column(u'patrimonio_obradearte', 'litografia', self.gf('django.db.models.fields.NullBooleanField')(null=True))

        # Renaming column for 'ObraDeArte.desperfectos' to match new field type.
        db.rename_column(u'patrimonio_obradearte', 'DESPERFECTOS', 'desperfectos')
        # Changing field 'ObraDeArte.desperfectos'
        db.alter_column(u'patrimonio_obradearte', 'desperfectos', self.gf('django.db.models.fields.TextField')())

        # Renaming column for 'ObraDeArte.estado_de_conservacion' to match new field type.
        db.rename_column(u'patrimonio_obradearte', 'ESTADO DE CONSERVACION', 'estado_de_conservacion')
        # Changing field 'ObraDeArte.estado_de_conservacion'
        db.alter_column(u'patrimonio_obradearte', 'estado_de_conservacion', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Renaming column for 'ObraDeArte.grabado' to match new field type.
        db.rename_column(u'patrimonio_obradearte', 'GRABADO', 'grabado')
        # Changing field 'ObraDeArte.grabado'
        db.alter_column(u'patrimonio_obradearte', 'grabado', self.gf('django.db.models.fields.NullBooleanField')(null=True))

        # Renaming column for 'ObraDeArte.medidas' to match new field type.
        db.rename_column(u'patrimonio_obradearte', 'MEDIDAS', 'medidas')
        # Changing field 'ObraDeArte.medidas'
        db.alter_column(u'patrimonio_obradearte', 'medidas', self.gf('django.db.models.fields.CharField')(max_length=100))

    def backwards(self, orm):

        # Renaming column for 'DisciplinaArtistica.disciplina' to match new field type.
        db.rename_column(u'patrimonio_disciplinaartistica', 'disciplina', 'DISCIPLINAS ARTISTICAS')
        # Changing field 'DisciplinaArtistica.disciplina'
        db.alter_column(u'patrimonio_disciplinaartistica', 'DISCIPLINAS ARTISTICAS', self.gf('django.db.models.fields.CharField')(max_length=50, db_column='DISCIPLINAS ARTISTICAS'))

        # Renaming column for 'ObraDeArte.imagen' to match new field type.
        db.rename_column(u'patrimonio_obradearte', 'imagen', 'IMAGEN')
        # Changing field 'ObraDeArte.imagen'
        db.alter_column(u'patrimonio_obradearte', 'IMAGEN', self.gf('django.db.models.fields.files.ImageField')(max_length=100, db_column='IMAGEN'))

        # Renaming column for 'ObraDeArte.otros' to match new field type.
        db.rename_column(u'patrimonio_obradearte', 'otros', 'OTROS')
        # Changing field 'ObraDeArte.otros'
        db.alter_column(u'patrimonio_obradearte', 'OTROS', self.gf('django.db.models.fields.NullBooleanField')(null=True, db_column='OTROS'))

        # Renaming column for 'ObraDeArte.pintura' to match new field type.
        db.rename_column(u'patrimonio_obradearte', 'pintura', 'PINTURA')
        # Changing field 'ObraDeArte.pintura'
        db.alter_column(u'patrimonio_obradearte', 'PINTURA', self.gf('django.db.models.fields.NullBooleanField')(null=True, db_column='PINTURA'))

        # Renaming column for 'ObraDeArte.tematica_y_estilo' to match new field type.
        db.rename_column(u'patrimonio_obradearte', 'tematica_y_estilo', 'TEMATICA Y ESTILO')
        # Changing field 'ObraDeArte.tematica_y_estilo'
        db.alter_column(u'patrimonio_obradearte', 'TEMATICA Y ESTILO', self.gf('django.db.models.fields.CharField')(max_length=50, db_column='TEMATICA Y ESTILO'))

        # Renaming column for 'ObraDeArte.fecha' to match new field type.
        db.rename_column(u'patrimonio_obradearte', 'fecha', 'FECHA')
        # Changing field 'ObraDeArte.fecha'
        db.alter_column(u'patrimonio_obradearte', 'FECHA', self.gf('django.db.models.fields.CharField')(max_length=100, db_column='FECHA'))

        # Renaming column for 'ObraDeArte.n_de_registro' to match new field type.
        db.rename_column(u'patrimonio_obradearte', 'n_de_registro', 'N DE REGISTRO')
        # Changing field 'ObraDeArte.n_de_registro'
        db.alter_column(u'patrimonio_obradearte', 'N DE REGISTRO', self.gf('django.db.models.fields.CharField')(max_length=50, db_column='N DE REGISTRO'))

        # Renaming column for 'ObraDeArte.ubicacion' to match new field type.
        db.rename_column(u'patrimonio_obradearte', 'ubicacion', 'UBICACION')
        # Changing field 'ObraDeArte.ubicacion'
        db.alter_column(u'patrimonio_obradearte', 'UBICACION', self.gf('django.db.models.fields.TextField')(db_column='UBICACION'))

        # Renaming column for 'ObraDeArte.titulo' to match new field type.
        db.rename_column(u'patrimonio_obradearte', 'titulo', 'TITULO')
        # Changing field 'ObraDeArte.titulo'
        db.alter_column(u'patrimonio_obradearte', 'TITULO', self.gf('django.db.models.fields.CharField')(max_length=255, db_column='TITULO'))

        # Renaming column for 'ObraDeArte.contacto' to match new field type.
        db.rename_column(u'patrimonio_obradearte', 'contacto', 'CONTACTO')
        # Changing field 'ObraDeArte.contacto'
        db.alter_column(u'patrimonio_obradearte', 'CONTACTO', self.gf('django.db.models.fields.TextField')(db_column='CONTACTO'))

        # Renaming column for 'ObraDeArte.observaciones' to match new field type.
        db.rename_column(u'patrimonio_obradearte', 'observaciones', 'OBSERVACIONES')
        # Changing field 'ObraDeArte.observaciones'
        db.alter_column(u'patrimonio_obradearte', 'OBSERVACIONES', self.gf('django.db.models.fields.TextField')(db_column='OBSERVACIONES'))

        # Renaming column for 'ObraDeArte.ceramica' to match new field type.
        db.rename_column(u'patrimonio_obradearte', 'ceramica', 'CERAMICA')
        # Changing field 'ObraDeArte.ceramica'
        db.alter_column(u'patrimonio_obradearte', 'CERAMICA', self.gf('django.db.models.fields.NullBooleanField')(null=True, db_column='CERAMICA'))

        # Renaming column for 'ObraDeArte.escultura' to match new field type.
        db.rename_column(u'patrimonio_obradearte', 'escultura', 'ESCULTURA')
        # Changing field 'ObraDeArte.escultura'
        db.alter_column(u'patrimonio_obradearte', 'ESCULTURA', self.gf('django.db.models.fields.NullBooleanField')(null=True, db_column='ESCULTURA'))

        # Renaming column for 'ObraDeArte.autor' to match new field type.
        db.rename_column(u'patrimonio_obradearte', 'autor', 'AUTOR')
        # Changing field 'ObraDeArte.autor'
        db.alter_column(u'patrimonio_obradearte', 'AUTOR', self.gf('django.db.models.fields.CharField')(max_length=50, db_column='AUTOR'))

        # Renaming column for 'ObraDeArte.fotografia' to match new field type.
        db.rename_column(u'patrimonio_obradearte', 'fotografia', 'FOTOGRAFIA')
        # Changing field 'ObraDeArte.fotografia'
        db.alter_column(u'patrimonio_obradearte', 'FOTOGRAFIA', self.gf('django.db.models.fields.NullBooleanField')(null=True, db_column='FOTOGRAFIA'))

        # Renaming column for 'ObraDeArte.dibujo' to match new field type.
        db.rename_column(u'patrimonio_obradearte', 'dibujo', 'DIBUJO')
        # Changing field 'ObraDeArte.dibujo'
        db.alter_column(u'patrimonio_obradearte', 'DIBUJO', self.gf('django.db.models.fields.NullBooleanField')(null=True, db_column='DIBUJO'))

        # Renaming column for 'ObraDeArte.tecnica' to match new field type.
        db.rename_column(u'patrimonio_obradearte', 'tecnica', 'TECNICA')
        # Changing field 'ObraDeArte.tecnica'
        db.alter_column(u'patrimonio_obradearte', 'TECNICA', self.gf('django.db.models.fields.CharField')(max_length=50, db_column='TECNICA'))

        # Renaming column for 'ObraDeArte.litografia' to match new field type.
        db.rename_column(u'patrimonio_obradearte', 'litografia', 'LITOGRAFIA')
        # Changing field 'ObraDeArte.litografia'
        db.alter_column(u'patrimonio_obradearte', 'LITOGRAFIA', self.gf('django.db.models.fields.NullBooleanField')(null=True, db_column='LITOGRAFIA'))

        # Renaming column for 'ObraDeArte.desperfectos' to match new field type.
        db.rename_column(u'patrimonio_obradearte', 'desperfectos', 'DESPERFECTOS')
        # Changing field 'ObraDeArte.desperfectos'
        db.alter_column(u'patrimonio_obradearte', 'DESPERFECTOS', self.gf('django.db.models.fields.TextField')(db_column='DESPERFECTOS'))

        # Renaming column for 'ObraDeArte.estado_de_conservacion' to match new field type.
        db.rename_column(u'patrimonio_obradearte', 'estado_de_conservacion', 'ESTADO DE CONSERVACION')
        # Changing field 'ObraDeArte.estado_de_conservacion'
        db.alter_column(u'patrimonio_obradearte', 'ESTADO DE CONSERVACION', self.gf('django.db.models.fields.CharField')(max_length=50, db_column='ESTADO DE CONSERVACION'))

        # Renaming column for 'ObraDeArte.grabado' to match new field type.
        db.rename_column(u'patrimonio_obradearte', 'grabado', 'GRABADO')
        # Changing field 'ObraDeArte.grabado'
        db.alter_column(u'patrimonio_obradearte', 'GRABADO', self.gf('django.db.models.fields.NullBooleanField')(null=True, db_column='GRABADO'))

        # Renaming column for 'ObraDeArte.medidas' to match new field type.
        db.rename_column(u'patrimonio_obradearte', 'medidas', 'MEDIDAS')
        # Changing field 'ObraDeArte.medidas'
        db.alter_column(u'patrimonio_obradearte', 'MEDIDAS', self.gf('django.db.models.fields.CharField')(max_length=100, db_column='MEDIDAS'))

    models = {
        u'patrimonio.disciplinaartistica': {
            'Meta': {'object_name': 'DisciplinaArtistica'},
            'disciplina': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "'Id'"})
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