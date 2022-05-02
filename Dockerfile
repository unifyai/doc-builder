FROM ubuntu:20.04

# create user
ARG user
ARG uid
RUN useradd -ms /bin/bash -u $uid $user

# non-interactive
ENV DEBIAN_FRONTEND=noninteractive

# installs
RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN apt-get install -y rsync
RUN pip3 install --upgrade pip
RUN pip3 install wheel setuptools
COPY requirements.txt /
RUN cat requirements.txt | xargs -n 1 pip3 install; exit 0

# set user
USER $user

# project directory
RUN mkdir /home/$user/ivy
RUN mkdir /home/$user/ivy/docs

# doc directories
COPY --chown=$user:$user docs /home/$user/global_docs
RUN mkdir /home/$user/project_docs

# working directory
WORKDIR /home/$user

# entry point
COPY --chown=$user:$user docs/entrypoint.sh /home/$user
ENTRYPOINT ["bash", "entrypoint.sh"]