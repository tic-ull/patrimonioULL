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

from fabric.api import env, sudo, local

env.project_name = 'patrimonioULL'
env.repo = 'https://bitbucket.org/rayco/patrimonioull'
env.branch = 'master'


def development():
    """Development Environment"""
    env.path = '~/PATRIMONIO-ULL'
    env.hosts = ['localhost']
    env.user = 'rayco'
    env.python_version = '2.7'


def install_dependences_requirements():
    sudo('apt-get install -y build-essential git python-dev libpq-dev')
    sudo('apt-get install -y postgresql postgresql-client postgresql-contrib')


def create_enviroment():
    local('mkdir -p %s/VIRTUALENV' % env.path)
    local('cd %s/VIRTUALENV && virtualenv --no-site-packages .' % env.path)


def setup():
    # Install PIP and VIRTUALENV
    sudo('apt-get install -y python-pip')
    sudo('pip install virtualenv')
    # Install Dependences
    install_dependences_requirements()
    # Create Enviroment
    create_enviroment()


def download():
    local('git clone -b %s %s %s/%s' % (
        env.branch, env.repo, env.path, env.project_name))


def install_requirements():
    local('. %s/VIRTUALENV/bin/activate && '
          'pip install -r requirements.txt -U' % env.path)


def collectstatic():
    local('. %s/VIRTUALENV/bin/activate && '
          'python manage.py collectstatic --noinput' % env.path)


def deploy():
    download()
    install_requirements()
