# -*- encoding: UTF-8 -*-

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

from django.contrib.admin.templatetags.admin_modify import register
from django.contrib.admin.templatetags.admin_modify import submit_row as osr


@register.inclusion_tag('admin/submit_line.html', takes_context=True)
def submit_row(context):
    ctx = osr(context)  # Here is Django's logic => it ignores the context
    if 'show_save_and_continue' in context:
        ctx['show_save_and_continue'] = context['show_save_and_continue']
    if 'show_save' in context:
        ctx['show_save'] = context['show_save']
    return ctx

import admin_advanced
import admin_basic
