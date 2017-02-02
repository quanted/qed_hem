import os
import sys

#this needs to be added so that the settings in the subdirectory django app can be found
root_path = os.path.abspath(os.path.split(__file__)[0])
sys.path.insert(0, os.path.join(root_path, 'splash_app'))
sys.path.insert(0, root_path)

if __name__ == "__main__":

    print('manage.py')

    if os.path.abspath(__file__) == os.path.join('/', 'var', 'www', 'ubertool', 'ubertool_eco', 'manage.py'):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings_apache")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings_local")

    from django.core.management import execute_from_command_line
    print(sys.argv)
    #wsgi needs to know about where the settings file is
    execute_from_command_line(sys.argv)
