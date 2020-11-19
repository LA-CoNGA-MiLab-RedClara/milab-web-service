# Builder image


# pull base image
FROM python:3.8.6-alpine as builder

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev jpeg-dev zlib-dev 

# lint
RUN pip install --upgrade pip
RUN pip install flake8
COPY . .
# RUN flake8 --ignore=E501,F401 .

# Install dependencies
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt


# Final image


FROM python:3.8.6-alpine

RUN mkdir -p /home/app

RUN addgroup -S app && adduser -S app -G app 

ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
RUN mkdir $APP_HOME/mediafiles
WORKDIR $APP_HOME

# Install dependencies
RUN apk update && apk add libpq musl-dev xmlsec libffi-dev libressl-dev gcc jpeg-dev zlib-dev
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --no-cache /wheels/*

COPY ./entrypoint.sh $APP_HOME
RUN chmod +x ./entrypoint.sh

COPY . $APP_HOME

RUN chown -R app:app $APP_HOME

USER app

ENTRYPOINT ["/home/app/web/entrypoint.sh"]
