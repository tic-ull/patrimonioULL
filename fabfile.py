# -*- coding: UTF-8 -*-

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
    sudo('mkdir -p %s/VIRTUALENV && cd %s/VIRTUALENV && virtualenv .' %
         (env.path, env.path))
    sudo('rm %s/VIRTUALENV/lib/python%s/no-global-site-packages.txt' %
         (env.path, env.python_version))
    sudo('cd %s && mkdir shared && mkdir releases' % (env.path))


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
