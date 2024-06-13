# Innovation Lab Project

## Prerequisites

Clone the repository with the command `git clone --recursive -j8 [url]`, because it contains submodules used in the repo

Or if the repo was already cloned, run `git submodule update --init`

Before running the scripts, make sure you have the following dependencies installed in the `requirements.txt`
or you can run `poetry install` to install them using `pypoetry`

After this, run poetry shell to create an environment that will contain all the deps you need for the execution of the 
scripts


# Docker usage

### Prerequisites

In your computer should be installed Docker.

---

In the root of the project, type the following terminal command:
  
``sudo docker-compose up -d``

#### Short explanation of the GUI
In the folder il_5safe/gui there is a folder called frontend  
Inside that you can find a web application, realized in VueJS (v2)

In the docker-compose.yml there are two principal containers, one that manage the backend (check Dockerfile_backend in the root path),
a simple container that executes a Flask python script that creates a route for being called by the frontend (check Dockerfile_frontend).

The docker-compose file pulls the images that are available in the dockerhub storage.
If something is wrong or not working, it is recommended to comment the rows 4 and 20 (the images directives), and build again everything on your own computer.

#### Build 

### Model trained (prerequisite)
Be sure to download and place the [model trained with our custom dataset](https://drive.google.com/file/d/1-Ztg5uGtJj1aiL50wM5aAQ3zCs7x2wcY/view?usp=sharing) in the folder `il_5safe/resources/weights/yolov5/best_model.pt`
before the build

### How to build the images
Execute the command `sudo docker-compose build --no-cache`.

For the multiplatform build: `docker buildx build --platform linux/amd64,linux/arm64 -f Dockerfile_backend --push --tag giorginogreg/innovationlab-5safe-be:latest .`

Then execute the command ``sudo docker-compose up -d``

--- 

### Execute the prediction

After the build / docker-compose up command is executed successfully, you can open the frontend interface in the browser via the link `http://localhost:8080`

Then, the interface will explain you the steps to execute, for example uploading an image and then clicking the prediction button after the model selection


Test command: /opt/poetry-venv/bin/python models/yolov5/detect.py --weights resources/weights/yolov5/best_model.pt --source uploaded_image.jpg --name uploaded_image --exist-ok