#fabric store
APPS_TO_WATCH = ['Media', 'User.Creations',  'User.Library', 'User.Account', 'User.Networks']
def initialmigration():
    for app in APPS_TO_WATCH:
        local('chmod +x manage.py')
        local('./manage.py schemamigration %s --initial' % app)
        
def automigration():
    for app in APPS_TO_WATCH:
        local('python manage.py schemamigration %s --auto' % app)

def migrate():
    for app in APPS_TO_WATCH:
        local('python manage.py migrate %s' % app)
    