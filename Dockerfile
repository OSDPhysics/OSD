FROM python:3.6.10-buster
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
  && rm -rf /var/lib/apt/lists/*
RUN pip install -r requirements.txt
ADD ./ /code/
CMD ["python", "OSD/manage.py", "runserver", "0.0.0.0:8001"]