FROM nginxinc/nginx-unprivileged:1-alpine

COPY ./default.conf /etc/nginx/conf.d/default.conf

USER root

RUN mkdir -p /static
RUN chmod 755 /static

# USER nginx
