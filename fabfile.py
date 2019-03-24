from fabric.api import *

env.user = 'dtat'
env.hosts = ['dtat.hampl.space']

def pack():
    # build the package
    local('python setup.py sdist --formats=gztar', capture=False)

def deploy():
    # figure out the package name and version
    dist = local('python setup.py --fullname', capture=True).strip()
    filename = '%s.tar.gz' % dist

    # upload the package to the temporary folder on the server
    put('dist/%s' % filename, '/home/dtat/tmp/%s' % filename)

    # install the package in the application's virtualenv with pip
    sudo('/home/dtat/www/dtat_main_server/venv/bin/pip install /home/dtat/tmp/%s' % filename)

    # migrate & upgrade
    # run('export FLASK_APP=dtat')
    run('cd /home/dtat/www/dtat_main_server/ && export FLASK_APP=dtat && /home/dtat/www/dtat_main_server/venv/bin/flask db migrate && /home/dtat/www/dtat_main_server/venv/bin/flask db upgrade')

    # remove the uploaded package
    run('rm -r /home/dtat/tmp/%s' % filename)

    #restart supervisor's subprocess
    sudo('sudo supervisorctl restart dtat-main-server')