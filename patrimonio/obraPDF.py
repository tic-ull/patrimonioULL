# -*- coding: UTF-8 -*-

#
#    Copyright 2013-2015
#
#      Rayco Abad-Martín <rayco.abad@gmail.com>
#      http://www.linkedin.com/in/rabad
#
#    This file is part of patrimonioULL.
#
#    patrimonioULL is free software: you can redistribute it and/or
#    modify it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    patrimonioULL is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with patrimonioULL.  If not, see
#    <http://www.gnu.org/licenses/>.
#

from .helpers import imagen_max_size
from django.conf import settings as st
from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch, mm
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer,
                                TableStyle)
from io import BytesIO
from slugify import slugify


class ObraPDF:
    BLUE_SECONDARY_ULL = colors.HexColor('#EBF3FA')
    BLUE_ULL = colors.HexColor('#006699')
    DEFAULT_FONT = 'Helvetica'
    DEFAULT_FONT_BOLD = 'Helvetica-Bold'
    DEFAULT_SPACER = 0.1 * inch
    HEADER_FONT_SIZE = 14
    MARGIN = 10 * mm
    PAGE_HEIGHT = A4[1]
    PAGE_NUMBERS_MARGIN = 0.75 * MARGIN
    PAGE_NUMBERS_SIZE = 8
    PAGE_WIDTH = A4[0]
    VIOLET_ULL = colors.HexColor('#7A3B7A')

    def __init__(self, obj):
        self.obj = obj

    def go(self):
        response = HttpResponse(content_type='application/pdf')
        filename = slugify(
            unicode(self.obj.pk) + "-" + self.obj.titulo) + ".pdf"
        response['Content-Disposition'] = (
            'attachment;' 'filename="%s"' % filename)

        buff = BytesIO()
        doc = SimpleDocTemplate(buff)
        story = [Spacer(1, 3 * self.DEFAULT_SPACER)]

        self.title(story)
        self.general_info(story)
        self.condition(story)
        self.location(story)
        self.observations(story)

        doc.build(
            story, onFirstPage=self.first_page, onLaterPages=self.later_pages)
        response.write(buff.getvalue())
        buff.close()
        return response

    def title(self, story):
        story.append(Paragraph(u'%s' % self.obj.titulo, self.style_h2()))
        story.append(Spacer(1, 1 * self.DEFAULT_SPACER))

    def general_info(self, story):
        story.append(Paragraph(u'INFORMACIÓN GENERAL', self.style_h3()))
        text = u''
        if self.obj.autor:
            text += u'<b>Autor:</b> %s <br/>' % self.obj.autor
        if self.obj.fecha:
            text += u'<b>Fecha de Ejecución:</b> %s <br/>' % self.obj.fecha
        if self.obj.medidas:
            text += u'<b>Medidas:</b> %s <br/>' % self.obj.medidas
        if self.obj.tematica:
            text += u'<b>Temática y Estilo:</b> %s <br/>' % self.obj.tematica
        if self.obj.tecnica:
            text += u'<b>Técnica:</b> %s <br/>' % self.obj.tecnica
        if self.obj.disciplina:
            text += u'<b>Disciplina:</b> %s <br/>' % self.obj.disciplina
        story.append(Paragraph(text, self.style_n()))
        story.append(Spacer(1, 1 * self.DEFAULT_SPACER))

    def condition(self, story):
        story.append(Paragraph(u'ESTADO DE CONSERVACIÓN', self.style_h3()))
        text = u''
        if self.obj.estado:
            text += u'<b>Estado:</b> %s <br/>' % self.obj.estado
        if self.obj.desperfectos:
            text += u'<b>Desperfectos:</b> %s <br/>' % self.obj.desperfectos
        story.append(Paragraph(text, self.style_n()))
        story.append(Spacer(1, 1 * self.DEFAULT_SPACER))

    def location(self, story):
        story.append(Paragraph(u'LOCALIZACIÓN', self.style_h3()))
        text = u''
        if self.obj.localizacion:
            text += u'<b>%s</b><br/>' % self.obj.localizacion
        if self.obj.ubicacion:
            text += u'<b>Ubicación:</b> %s<br/>' % self.obj.ubicacion
        if self.obj.contacto:
            text += u'<b>Contacto:</b> %s <br/>' % self.obj.contacto
        story.append(Paragraph(text, self.style_n()))
        story.append(Spacer(1, 1 * self.DEFAULT_SPACER))

    def observations(self, story):
        if self.obj.observaciones:
            story.append(Paragraph(u'OBSERVACIONES', self.style_h3()))
            text = u'%s<br/>' % self.obj.observaciones
            story.append(Paragraph(text, self.style_n()))
            story.append(Spacer(1, 1 * self.DEFAULT_SPACER))

    # -------------------------------------------------------------------------
    # CONFIGURACIÓN DE LAS PÁGINAS
    # -------------------------------------------------------------------------

    def first_page(self, canvas, doc):
        canvas.saveState()
        self.header(canvas)
        canvas.restoreState()

    def later_pages(self, canvas, doc):
        canvas.saveState()
        self.header(canvas)
        canvas.setFont(self.DEFAULT_FONT, self.PAGE_NUMBERS_SIZE)
        canvas.drawCentredString(self.PAGE_WIDTH / 2.0,
                                 self.PAGE_NUMBERS_MARGIN,
                                 u'Página %s - %s' % (
                                     doc.page,
                                     self.obj.titulo
                                 ))
        canvas.restoreState()

    def header(self, canvas):
        canvas.setFont(self.DEFAULT_FONT_BOLD, self.HEADER_FONT_SIZE)
        canvas.setFillColor(self.BLUE_ULL)
        canvas.drawString(
            self.MARGIN, self.PAGE_HEIGHT - 2 * self.MARGIN,
            u'FICHA DE INVENTARIO: ' + unicode(self.obj.registro))
        if self.obj.imagen:
            thumb_width, thumb_height = imagen_max_size(
                self.obj.imagen, st.MAX_THUMB_SIZE)
            canvas.drawImage(
                self.obj.imagen.path,
                self.PAGE_WIDTH - self.MARGIN - thumb_width,
                self.PAGE_HEIGHT - thumb_height - self.MARGIN,
                thumb_width,
                thumb_height)

    # --------------------------------------------------------------------
    # ESTILOS DEL PDF
    # --------------------------------------------------------------------

    def style_n(self):
        style = getSampleStyleSheet()['Normal']
        style.leading = 12
        style.allowWidows = 0
        style.spaceBefore = 0.2 * inch
        return style

    def style_h3(self):
        style = getSampleStyleSheet()['Heading3']
        style.textColor = self.VIOLET_ULL
        return style

    def style_h2(self):
        style = getSampleStyleSheet()['Heading2']
        style.textColor = self.BLUE_ULL
        return style

    def style_table(self):
        style = TableStyle(
            [('SIZE', (0, 0), (-1, -1), 8),
             ('BOX', (0, 0), (-1, -1), 0.2, self.BLUE_ULL),
             ('LINEABOVE', (0, 0), (-1, -1), 0.2, self.BLUE_ULL),
             ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
             ('BACKGROUND', (0, 0), (-1, 0), self.BLUE_ULL),
             ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
             ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white,
                                                   self.BLUE_SECONDARY_ULL])]
        )
        return style
