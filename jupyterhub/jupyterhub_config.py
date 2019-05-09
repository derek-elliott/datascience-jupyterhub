import os
from jupyterhub.auth import DummyAuthenticator

c.JupyterHub.authenticator_class = DummyAuthenticator
c.Authenticator.admin_users = [os.environ['ADMIN_USER']]

c.Spawner.default_url = '/lab'
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.network_name = os.environ['DOCKER_NETWORK_NAME']
c.DockerSpawner.image_whitelist = {
    'GPU Enabled Data Science Notebook': 'saywhat1/jupyter-datascience:latest',
    'Minimal Notebook' : 'jupyter/minimal-notebook:2662627f26e0',
    'R Notebook': 'jupyter/r-ntoebook:2662627f26e0',
    'Scipy Notebook': 'jupyter/scipy-noteobok:2662627f26e0',
    'Tensorflow Notebook(CPU Only)': 'jupyter/tensorflow-notebook:2662627f26e0',
    'Data Science Notebook': 'jupyter/datascience-notebook:2662627f26e0'
}

notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/jovyan'
c.DockerSpawner.notebook_dir = notebook_dir
c.DockerSpawner.volumes = {'jupyterhub-user-{username}': notebook_dir}

c.JupyterHub.hub_ip = os.environ['HUB_IP']

c.JupyterHub.services = [
    {
        'name': 'cull_idle',
        'admin': True,
        'command': 'python /srv/jupyterhub/cull_idle_servers.py --timeout=3600'.split(),
    },
]
