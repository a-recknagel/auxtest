FROM python:3.7-alpine

LABEL maintainer="Arne Recknagel"

COPY wheelhouse/* wheelhouse/

RUN pip install wheelhouse/*

CMD [ "auxtest", "run", "--host", "0.0.0.0" ]
