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

from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User, Group


class CustomUserForm(UserChangeForm):

    permissions = forms.MultipleChoiceField(
        label=u'Permisos', required=False,
    )

    def __init__(self, *args, **kwargs):
        super(CustomUserForm, self).__init__(*args, **kwargs)
        lst = list()
        for perm in self.instance.get_all_permissions():
            p = (perm, perm)
            lst.append(p)
        self.fields['permissions'].choices = lst
        self.fields['permissions'].initial = lst


class CustomGroupForm(forms.ModelForm):

    users = forms.ModelMultipleChoiceField(
        label=u'Usuarios',
        queryset=User.objects.all(),
        required=False,
        widget=FilteredSelectMultiple(
            verbose_name=u'Usuarios',
            is_stacked=False,
        )
    )

    class Meta:
        model = Group
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CustomGroupForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['users'].initial = self.instance.user_set.all()

    def save(self, commit=True):
        group = super(CustomGroupForm, self).save(commit=False)
        if commit:
            group.save()
        if group.pk:
            group.user_set = self.cleaned_data['users']
            self.save_m2m()
        return group
