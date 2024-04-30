FROM python:3.12
# actually python image is debian based
 
ENV DEBIAN_FRONTEND noninteractive
RUN pip install --upgrade pip

# Install ffmpeg
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y ffmpeg

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR .

COPY requirements.txt ./
RUN pip install -r requirements.txt --no-cache-dir

COPY . .
