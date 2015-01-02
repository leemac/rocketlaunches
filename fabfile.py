from fabric.api import *


def deploy():
    code_dir = '/srv/www/rocketlaunches.org'
    with cd(code_dir):
        run("git pull origin master")    
        run('sudo pip install -r requirements.txt')      
        run('python manage.py syncdb --noinput')      

# Start, Restart, stop

def start_server():
    run_dir = '/srv/www/rocketlaunches.org'
    with cd(run_dir):
        run("uwsgi --ini jobsite.ini")   

def restart_server():
    run_dir = '/srv/www/'
    with cd(run_dir):
        run("kill -HUP `cat /tmp/rocketlaunches.org/rocketlaunches.org`")      

def stop_server():
    run_dir = '/srv/www/'
    with cd(run_dir):
        run("uwsgi --stop /tmp/rocketlaunches.org/rocketlaunches.org")    