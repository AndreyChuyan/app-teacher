#!/bin/bash
sudo docker stop app-teacher
sudo docker rm app-teacher
sudo docker build -t my_project .
sudo docker run -d --name app-teacher --log-driver=json-file -p 4441:8000 my_project