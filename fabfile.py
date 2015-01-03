from fabric.api import *


def deploy():
    code_dir = '/srv/www/rocketlaunches.org'
    with cd(code_dir):
        run("git pull origin master")    
        run('sudo pip install -r requirements.txt')      
        run('python rocketlaunches/manage.py migrate')      

# Start, Restart, stop

def start_server():
    with cd(run_dir):
        run("uwsgi --ini /srv/www/rocketlaunches.org/rocketlaunches/rocketapp.ini")   

def restart_server():
    with cd(run_dir):
        run("kill -HUP `cat /tmp/rocketlaunches.pid`")      

def stop_server():
    with cd(run_dir):
        run("uwsgi --stop /tmp/rocketlaunches.pid")    