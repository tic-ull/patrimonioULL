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

from django.conf import settings as st

import os


def content_file_name(instance, filename, side):
    extension = os.path.splitext(filename)[1]
    path = 'patrimonio/images/%s/%s_%s%s' % (
        instance.disciplina_id, instance.pk, side, extension)
    # Deleting the previous file, it doesn't rename with _number
    fullpath = os.path.join(st.MEDIA_ROOT, path)
    if os.path.exists(fullpath):
        os.remove(fullpath)
    return path


def name_front(instance, filename):
    return content_file_name(instance, filename, 'front')


def name_back(instance, filename):
    return content_file_name(instance, filename, 'back')


def imagen_max_size(imagen, max_size):
    if imagen:
        max_imagen_size = max(imagen.width, imagen.height)
        ratio = (max_imagen_size > max_size and
                 float(max_imagen_size) / max_size or 1)
        width = imagen.width / ratio
        height = imagen.height / ratio
        return width, height
