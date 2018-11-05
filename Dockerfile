FROM python:3.6-alpine

LABEL maintainer="Arne Recknagel"

COPY wheel/* wheel/
COPY logger_config.json .

RUN pip install wheel/*

CMD [ "python", "-m", "auxtest", "dev" ]
