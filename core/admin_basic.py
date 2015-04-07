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

from django.contrib.admin.sites import AdminSite
from django.contrib.auth.decorators import login_required


class BasicAdminSite(AdminSite):
    site_header = u'Administración Básica'

    def has_permission(self, request):
        return request.user.has_perm('auth.basic_staff')

basic_admin_site = BasicAdminSite(name='basic_admin')
basic_admin_site.login = login_required(basic_admin_site.login)
