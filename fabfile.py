from fabric.api import *

def deploy():
    run_dir = '/srv/www/rocketlaunches.org'
    with cd(run_dir):
        run("git pull origin master")    
        run('sudo pip install -r requirements.txt')      
        run('python3 rocketlaunches/manage.py migrate')      

# Start, Restart, stop

def start_server():
    run_dir = '/srv/www/'
    with cd(run_dir):
        run("uwsgi --ini /srv/www/rocketlaunches.org/rocketlaunches/rocketapp.ini")   

def restart_server():
    run_dir = '/srv/www/'
    with cd(run_dir):
        run("kill -HUP `cat /tmp/rocketlaunches.pid`")      

def stop_server():
    run_dir = '/srv/www/rocketlaunches.org/rocketlaunches'
    with cd(run_dir):
        run("uwsgi --stop /tmp/rocketlaunches.pid")    

def build():
    run_dir = '/srv/www/rocketlaunches.org/'
    with cd(run_dir):
        run("app.build/r.js -o build.js")    

def update_data():
    run_dir = '/srv/www/rocketlaunches.org/rocketlaunches'
    with cd(run_dir):
        run("python3 manage.py migrate --settings=rocketlaunches.settings.production")    
        run("python3 manage.py loaddata rockets.json --settings=rocketlaunches.settings.production")    
        run("python3 manage.py import_data --settings=rocketlaunches.settings.production")    