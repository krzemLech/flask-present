#!/bin/bash

set -a
. .env
sudo docker build --tag flask-present .
sudo docker run -p 5001:5000 flask-present