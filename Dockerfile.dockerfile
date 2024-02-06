# Container image that runs your code
FROM alpine:3.18

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY . /.