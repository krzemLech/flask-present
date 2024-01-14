FROM python:3.8-slim-buster

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

EXPOSE 5000

ENV FLASK_ENV=production
ENV DB_URI=$DB_URI
ENV SECRET_KEY=$SECRET_KEY

RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["sh", "entrypoint.sh"]