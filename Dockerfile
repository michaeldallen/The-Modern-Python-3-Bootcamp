FROM ubuntu:bionic
RUN apt-get update && apt-get -y dist-upgrade
RUN apt-get install --assume-yes \
  make \
  bsdmainutils curl

RUN apt-get update && apt-get upgrade -y

