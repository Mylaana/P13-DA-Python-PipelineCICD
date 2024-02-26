# Start your image with a node base image
FROM python:3.13.0a4-alpine3.19

ENV PATH="/scripts:${PATH}"

RUN pip install --upgrade pip

COPY . .

RUN pip install -r requirements.txt

# COPY ./scripts /scripts

RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser -D user
RUN chown -R user:user /vol
RUN chmod -R 755 /vol/web

# USER user

CMD ["sh", "/scripts/docker/entrypoint.sh"]
