FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip \
  && apt-get install -y httrack curl \
  && apt-get install -y texlive-latex-base \
  && apt-get install -y texlive-fonts-recommended \
  && apt-get install -y texlive-fonts-extra \
  && apt-get install -y texlive-latex-extra

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY cv_builder .

CMD [ "python", "manage.py", "runserver" ]