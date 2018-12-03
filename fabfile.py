from fabric.api import abort, cd, env, local, run, settings, task
from fabric.contrib.console import confirm
from fabric.operations import prompt

env.use_ssh_config = True
env.hosts = ["webfaction"]

project_name = "grace"
python_version = "3.7"


env.remote_app_dir = f'/home/paloni/webapps/{project_name}_project/{project_name}/'
env.remote_app_static_dir = f'/home/paloni/webapps/{project_name}_static/'
env.remote_apache_dir = '/home/paloni/webapps/{project_name}_project/apache2/'


def run_command(command):
    return f"python manage.py {command} --settings={project_name}.settings.local"


@task
def runserver():
    local(run_command('runserver'))


@task
def makemigrations():
    local(run_command('makemigrations'))


@task
def migrate():
    local(run_command('migrate'))


@task
def deploy():
    """Runing tests
    Commit changes
    Push to the git server
    Deploy to the server
    """

    test_results = test()
    commit()
    push()
    if test_results:
        deploy_to_server()


@task
def cmt():
    """Commits and push changes to the git server after running tests
    """

    test_results = test()
    if test_results:
        commit()
        push()


def test():
    with settings(warn_only=True):
        result = local(
            f"python manage.py test --settings={project_name}.settings.test")
        if result.failed and not confirm("Tests failed. Continue?"):
            abort("Aborted at user request.")
            return False
        else:
            return True


def push():
    local("git push origin master")


def commit():
    message = prompt("Enter a git commit message: ")
    local('git add . && git commit -am "{}"'.format(message))


def deploy_to_server():
    with cd(f'{env.remote_app_dir}'):
        run('git pull origin master')

    manage_py = f'cd {env.remote_app_dir}/{project_name}/; python{python_version} manage.py'
    
    run(f'{manage_py} migrate --settings={project_name}.settings.production')
    run(f'{manage_py} collectstatic --settings={project_name}.settings.production --noinput')

    run(f'cd {env.remote_app_dir}/{project_name}/{project_name}/; touch wsgi.py;')
