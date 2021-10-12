FROM python:3.10.0-slim-buster
RUN apt-get update && apt-get upgrade -y
RUN apt-get install git curl python3-pip ffmpeg -y
RUN python3.10 -m pip install -U pip
COPY . /app
WORKDIR /app
RUN python3.10 -m pip install -U -r requirements.txt
CMD python3.10 -m VoiceChat_Song_bot
