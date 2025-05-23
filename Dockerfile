# Ubuntu

FROM ubuntu:24.04
RUN apt-get update && apt-get -y dist-upgrade
RUN apt-get update && apt-get -y install \
    \
    bsdmainutils \
    curl \
    make \
    python3 \
    python3-pip \
    \
    cowsay



# Python

RUN pip3 install \
    \
    click \
    \
    pytest 



# execution

WORKDIR /workdir

#EOF
