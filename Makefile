server:
	docker-compose --env-file config.env --profile server up -d --build

client: 
	docker-compose --profile client up -d --build

stop:
	docker-compose --env-file config.env --profile server  --profile client down

restart:
	make stop
	make server
	make client

connect_client:
	docker exec -it mlflow_client bash

generate-dockerfile:
	mlflow models generate-dockerfile -m '${model_uri}' -d 'model_images/${model_name}-dockerfile'

build-docker:
	docker build -t '${model_name}'  'model_images/${model_name}-dockerfile'

run_docker_model:
	docker run -p ${port}:8080 ${model_name}

serve_model:
	make build-docker model_name='${model_name}'
	make run_docker_model port=${port} model_name='${model_name}'
