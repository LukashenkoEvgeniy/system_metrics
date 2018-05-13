FROM python:3
MAINTAINER Lukashenko Yevhenii <freewindsua@gmail.com>

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY system_metrics.py /usr/src/app
 
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "system_metrics.py"]