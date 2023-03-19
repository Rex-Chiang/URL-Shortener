FROM python:3.8.2
ENV PYTHONUNBUFFERED=1
RUN mkdir /backend
WORKDIR /backend
ADD . /backend
RUN pip3 install -r requirements.txt