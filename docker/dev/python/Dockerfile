FROM python:3.7-slim-buster

ENV PYTHONUNBUFFERED=1

ARG requirements=requirements/dev.txt

RUN mkdir -p /opt/oracle

WORKDIR /opt/oracle
RUN apt-get update && apt-get install -y libaio1 wget unzip \
    && wget --quiet https://download.oracle.com/otn_software/linux/instantclient/instantclient-basiclite-linuxx64.zip \
    && unzip instantclient-basiclite-linuxx64.zip \
    && rm -f instantclient-basiclite-linuxx64.zip \
    && cd instantclient* \
    && rm -f *jdbc* *occi* *mysql* *README *jar uidrvci genezi adrci \
    && echo /opt/oracle/instantclient* > /etc/ld.so.conf.d/oracle-instantclient.conf \
    && ldconfig

WORKDIR /src

COPY ./src /src

COPY ./docker/dev/python/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

RUN pip install --no-cache-dir -r ${requirements}

ENTRYPOINT ["/entrypoint.sh"]