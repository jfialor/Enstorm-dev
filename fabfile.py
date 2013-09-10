#from fabric.api import local

def prepare_deployment(branch_name):
    local('python manage.py test Media')
    local('git add -p && git commit')
    local('git checkout master && git merge ' + branch_name)
    
#from fabric.api import lcd
from fabric.api import *

def deploy():
    with lcd('/Users/SedemFialor/documents/binary/TheBrew'):
        local('git pull /Users/SedemFialor/documents/binary/dev/TheBrew')
        #local('python manage.py migrate Media')
        #local('python manage.py test Media')
        with lcd('/Users/SedemFialor/documents/binary/TheBrew/Enstorm'):
            local('python manage.py syncdb')
            local('python manage.py runserver')
            
def r():
    with lcd('/Users/SedemFialor/documents/binary/dev/TheBrew/Enstorm'):
        local('python manage.py runserver')