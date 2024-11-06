# mlflow_docker
This repository has the code of my mlflow studies with Alura

The makefile have the basic make commands to run the services.

Everything is set in the docker-compose.yaml.

The basic idea is: we have 4 containers:
- A postgres DB
- Minio playing as a S3 storage.
- A Mlflow tracking server
- A Mlflow client, running a jupyter notebook.

As a plus, 'make serve-model' command serves a model as a standalone container 
