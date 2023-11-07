from concurrent.futures import ThreadPoolExecutor
from fabric import Connection
import os

def deploy_task(command, host, user, password):
    with Connection(host=host, user=user, connect_kwargs={"password": password}) as conn:
        conn.run(command)

def deploy_to_instance(host, user, password):
    commands = [
        "git remote add origin https://github.com/sanket0770/Bloglib.git",
        "git pull origin main",
        "pip install -r requirements.txt",
        "python manage.py migrate",
        "python manage.py collectstatic --noinput",
        "sudo systemctl restart gunicorn"
        # Additional deployment tasks as needed
    ]

    with ThreadPoolExecutor(max_workers=len(commands)) as executor:
        executor.map(lambda cmd: deploy_task(cmd, host, user, password), commands)

def deploy():
    host = os.getenv('HOST')  # Get host from environment variables
    user = os.getenv('SSH_USER')  # Get SSH username from environment variables
    password = os.getenv('SSH_PASSWORD')  # Get SSH password from environment variables

    deploy_to_instance(host, user, password)

# Run the deployment script
deploy()
