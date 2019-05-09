# JupyterHub project with CUDA enabled JupyterLab notebook

## Description
This project sets up a JupyterHub instance in a Docker container that uses the DockerSpawner to spin up single user notebooks.  This will mount a volume named after each user in their notebook to `/home/jovyan` to persist their work.

## Build
Make sure to create a .env file in the base of this repository with the following variables:
```
COMPOSE_PROJECT_NAME=
ADMIN_USER=
DOCKER_REPO=
TRAEFIK_DOCKER_NETWORK=
```
Then run the command `docker-compose build`.  The `jupyterlab` image takes some time to build.  It is available from `saywhat1/jupyter-datascience:latest`, so it can be pulled and tagged under your desired Docker repo.

Run `docker-compose up -d` and open a browser to `hub.localhost`.  If you don't have Traefik started and configured to discover Docker containers, you can modify `docker-compose.yml` to expose the port 8000 and open a browser to `localhost:8000`.  This is using the DummyAuthenticator, so anyone that is able to reach the DockerHub page will be able to login and launch a notebook.
