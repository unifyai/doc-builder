FROM ubuntu:22.04

# non-interactive
ENV DEBIAN_FRONTEND=noninteractive

# installs
RUN apt-get update
RUN apt-get install -y python3-dev python3-pip
RUN apt-get install -y rsync
RUN pip3 install --upgrade pip
RUN pip3 install wheel setuptools

RUN mkdir /doc-builder
WORKDIR /doc-builder

COPY . /doc-builder

RUN pip3 install -r requirements.txt

RUN mkdir /project
ENTRYPOINT [ "./docker_entrypoint.sh" ]
