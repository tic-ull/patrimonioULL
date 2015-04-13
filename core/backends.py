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

from django.conf import settings as st
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django_cas_ng.backends import _verify

import django_cas_ng


class CASBackend(django_cas_ng.backends.CASBackend, ModelBackend):

    def authenticate(self, ticket, service, request):
        """Verifies CAS ticket and gets or creates User object"""
        username, attributes = _verify(ticket, service)
        # If we don't have the user's document we'll not allow him to do login
        if (not attributes or 'NumDocumento' not in attributes
                or attributes['NumDocumento'] is None):
            st.CAS_RETRY_LOGIN = False
            return None
        # If type of account of the user isn't allow then
        # we will not allow him to do login
        if (attributes and 'TipoCuenta' in attributes
                and attributes['TipoCuenta'] in st.CAS_TIPO_CUENTA_NOAUT):
            st.CAS_RETRY_LOGIN = False
            return None
        request.session['attributes'] = attributes
        return User.objects.get_or_create(username=username)[0]
