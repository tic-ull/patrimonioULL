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
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^patrimonioarte/admin/', include(admin.site.urls)),
    url(r'^patrimonioarte/tinymce/', include('tinymce.urls')),
    url(r'^patrimonioarte/accounts/login/$',
        'django_cas.views.login', name='login'),
    url(r'^patrimonioarte/accounts/logout/$',
        'django_cas.views.logout', name='logout'),
]

if st.DEBUG:
    urlpatterns += static(st.MEDIA_URL, document_root=st.MEDIA_ROOT)
