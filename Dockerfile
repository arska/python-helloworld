# Dockerfile
# inherit from this "empty base image", see https://hub.docker.com/_/python/
FROM python:alpine
MAINTAINER Aarno Aukia <aarno.aukia@vshn.ch>
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# run this command at run-time
CMD [ "python", "app.py" ]
# expose this TCP-port
EXPOSE 3000
# make this path persistent between versions of the container - not needed in this example
# VOLUME /usr/src/app/mypersistentdatavolume/

