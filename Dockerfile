# Dockerfile
# inherit from this "empty base image", see https://hub.docker.com/_/python/
FROM python:3-onbuild
# who takes care of this ?
MAINTAINER Aarno Aukia <aarno.aukia@vshn.ch>
# add all files from this git to path inside container - default
#ADD . /usr/src/app/
# run this command inside container at build-time - default
#RUN pip install -r /usr/src/app/requirements.txt
# run this command at run-time
CMD [ "python", "app.py" ]
# expose this TCP-port
EXPOSE 8080
# make this path persistent between versions of the container - not needed in this example
# VOLUME /usr/src/app/mypersistentdatavolume/

