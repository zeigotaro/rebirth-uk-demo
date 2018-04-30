.PHONY: build run inspect

IMAGE_NAME = rebirth-uk-demo
IMAGE_TAG = latest
REPO_URL = rebirth.azurecr.io/demo
CONTAINER_NAME = uk-demo

build:
	sudo docker build -t $(REPO_URL)/$(IMAGE_NAME):$(IMAGE_TAG) . 

push:
	sudo docker push $(REPO_URL)/$(IMAGE_NAME):$(IMAGE_TAG)

run: 
	sudo docker run --rm -p 5000:5000 --name $(CONTAINER_NAME) $(REPO_URL)/$(IMAGE_NAME)
