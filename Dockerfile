FROM python:2.7.18-slim

RUN mkdir /code
COPY . /code
WORKDIR /code


RUN pip install -r requirements.txt


ENTRYPOINT ["/code/entrypoint.sh"]
