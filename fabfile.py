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

from fabric.api import env, sudo

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
    sudo('apt-get install -y build-essential python-dev git')


def create_enviroment():
    sudo('mkdir -p %s/VIRTUALENV' % env.path)
    sudo('cd %s/VIRTUALENV && virtualenv --no-site-packages .' % env.path)
    sudo('cd %s && mkdir shared && mkdir releases' % env.path)


def setup():
    # Install PIP and VIRTUALENV
    sudo('apt-get install -y python-pip')
    sudo('pip install virtualenv')
    # Install Dependences
    install_dependences_requirements()
    # Create Enviroment
    create_enviroment()


def version():
    import time
    env.release = str(env.branch) + '-' + str(time.strftime('%Y%m%d%H%M%S'))


def download():
    version()
    sudo('git clone -b %s %s %s/releases/%s' %
         (env.branch, env.repo, env.path, env.release))


def install_requirements():
    sudo('source %s/VIRTUALENV/bin/activate && \
          pip install -r %s/releases/%s/requirements.txt' %
         (env.path, env.path, env.release))


def symlink_current_release():
    sudo('rm -rf %s/%s' % (env.path, env.project_name))
    sudo('ln -s %s/releases/%s %s/%s' %
         (env.path, env.release, env.path, env.project_name))

    sudo('rm -rf %s/%s/media/patrimonio' % (env.path, env.project_name))
    sudo('ln -s %s/shared/media/patrimonio %s/%s/media/' %
         (env.path, env.path, env.project_name))

    sudo('rm -rf %s/%s/%s/settings_local.py' %
         (env.path, env.project_name, env.project_name))
    sudo('ln -s %s/shared/settings_local.py %s/%s/%s/' %
         (env.path, env.path, env.project_name, env.project_name))


def deploy():
    download()
    install_requirements()
    symlink_current_release()
