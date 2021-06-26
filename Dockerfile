FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip
  && apt-get install -y httrack
  && apt-get install texlive-latex-base
  && apt-get install texlive-fonts-recommended
  && apt-get install texlive-fonts-extra
  && apt-get install texlive-latex-extra

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .


CMD [ "python", "manage.py", "runserver" ]