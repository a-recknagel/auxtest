FROM python:3.6-alpine

LABEL maintainer="Arne Recknagel"

COPY wheel/* wheel/

RUN pip install wheel/*

CMD [ "python", "-m", "auxtest", "serve" ]
