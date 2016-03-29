# start with a base image
FROM django:1.9.4-python2
MAINTAINER epicallan <epicallan.al@gmail.com>

RUN mkdir /src
WORKDIR /src
ADD ./apps /src

# install dependencies
RUN apt-get update
RUN pip install argparse==1.2.1 djangorestframework==3.1.1 wsgiref==0.1.2 gunicorn==19.4.5

CMD gunicorn -w 2 -b 0.0.0.0:8080 root.wsgi
