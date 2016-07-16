FROM evild/alpine-python:3.5

ENV PYTHONUNBUFFERED=TRUE

RUN mkdir -p /app /app/logs
WORKDIR /app

ADD ./requirements.txt /app/
RUN pip install -r /app/requirements.txt

COPY . /app

VOLUME ["/app"]

EXPOSE 8001

CMD gunicorn run -c /app/app/settings.py
