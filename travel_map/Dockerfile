FROM python:3.9.0-slim-buster

COPY requirements.txt /tmp

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    apache2 \
    apache2-dev && \
    apt-get clean && \
    pip3 install --upgrade pip && \
    pip3 install -r /tmp/requirements.txt

COPY config/flask.conf /etc/apache2/sites-available/

RUN a2ensite flask

EXPOSE 80

CMD [ "/usr/sbin/apachectl", "-D", "FOREGROUND"]
