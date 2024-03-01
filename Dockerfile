# Start your image with a node base image
FROM python:3.13.0a4-alpine3.19

ENV PATH="/scripts:${PATH}"

RUN pip install --upgrade pip

COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

RUN mkdir /app
COPY ./app /app
WORKDIR /app

COPY ./scripts /scripts
RUN chmod +x /scripts/*


RUN mkdir -p /vol/media
RUN mkdir -p /vol/static

RUN adduser -D user

RUN chown -R user:user /vol
RUN chmod -R 755 /vol

RUN chown -R user:user /app
RUN chmod -R 755 /app

# USER user

CMD ["sh", "/scripts/docker/entrypoint.sh"]
