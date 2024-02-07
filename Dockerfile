# Start your image with a node base image
FROM python:3-alpine3.19

COPY . .

RUN pip install -r requirements.txt
# CMD echo "running python file:";python "./main.py"
