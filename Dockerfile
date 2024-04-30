# Stage 1: Build Stage
FROM python:slim-bullseye

WORKDIR /bcra-app

COPY requirements.txt requirements.txt
#RUN apt-get update -y
#RUN apt-get update && apt-get install -y python3-pip
#RUN apt-get autoremove -y
#RUN apt-get clean
RUN pip3 install -r requirements.txt
COPY . .

EXPOSE 5000

CMD [ "python3", "index.py"]