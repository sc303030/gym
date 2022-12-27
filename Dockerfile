FROM python:3.11-slim
ENV PYTHONUNBUFFERED=1
RUN apt-get update && apt-get install python3-dev default-libmysqlclient-dev gcc  -y
COPY . /gym
WORKDIR /gym
RUN pip install -r requirements.txt && pip install cryptography
ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /