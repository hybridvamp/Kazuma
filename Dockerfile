FROM python:3.10.6-slim-buster

WORKDIR .
COPY . .

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

RUN pip3 install -r requirements.txt

CMD ["python3", "mage.py"]