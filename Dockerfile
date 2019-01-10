 FROM python:3.5.2
 ENV PYTHONUNBUFFERED 1
 
 RUN mkdir /code
 WORKDIR /code
 
 # Installing OS Dependencies
 RUN apt-get update && apt-get upgrade -y && apt-get install -y libsqlite3-dev
 
 RUN pip install -U pip setuptools
 
 ADD requirements.txt /code/
 
 RUN pip install --upgrade pip
 RUN pip install -r /code/requirements.txt
 
 ADD . /code/

