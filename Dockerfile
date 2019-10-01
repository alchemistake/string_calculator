FROM alpine:3.8
MAINTAINER Caner Caliskaner

# Install dependencies
RUN apk update && apk add nginx uwsgi-python3 supervisor

COPY ./requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

# Setup directory structure
COPY ./backend ./backend

COPY ./deployment/nginx-base.conf /etc/nginx/nginx.conf
COPY ./deployment/nginx.conf /etc/nginx/conf.d/nginx.conf
COPY ./deployment/uwsgi-base.ini /etc/uwsgi/uwsgi.ini
COPY ./deployment/supervisord.ini /etc/supervisor.d/supervisord.ini
COPY ./deployment/entrypoint.sh ./entrypoint.sh
RUN chmod +x ./entrypoint.sh

COPY ./deployment/uwsgi.ini ./backend

ENV PYTHONUNBUFFERED 1
ENV UWSGI_CHEAPER 2
ENV UWSGI_PROCESSES 16
ENV UWSGI_INI /backend/uwsgi.ini

ENTRYPOINT ["./entrypoint.sh"]
CMD ["/usr/bin/supervisord"]
