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

from .forms import CustomUserForm, CustomGroupForm
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group


def remove_fieldsets(cls, field_name, message=None, new_field=None):
    """Remove a field from the fieldset of an Admin class"""
    lst = list(cls.fieldsets)
    for sets in lst:
        if field_name in sets[1]['fields']:
            field = list(sets[1]['fields'])
            field.remove(field_name)
            if new_field is not None:
                field.append(new_field)
            sets[1]['fields'] = tuple(field)
            if message is not None:
                sets[1]['description'] = message
    return tuple(lst)


class CustomUserAdmin(UserAdmin):

    form = CustomUserForm

    list_display = ('username', 'first_name', 'last_name', 'email',
                    'is_active', 'is_staff')

    readonly_fields = ('first_name', 'last_name', 'email')

    fieldsets = remove_fieldsets(
        cls=UserAdmin, field_name='user_permissions', new_field='permissions')

    list_filter = UserAdmin.list_filter + ('groups__name', )


class CustomGroupAdmin(GroupAdmin):
    form = CustomGroupForm

    def membership(self):
        return self.user_set.count()
    membership.short_description = u'Número de miembros'
    membership.allow_tags = True

    list_display = ('name', membership, )

admin.site.login = login_required(admin.site.login)
admin.site.site_url = None

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.unregister(Group)
admin.site.register(Group, CustomGroupAdmin)
