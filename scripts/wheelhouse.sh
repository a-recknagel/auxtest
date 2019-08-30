#!/usr/bin/env bash
set -euf -o pipefail

# get location of project root
PROJECT_DIR="$(dirname "$(dirname "$(readlink -f "${0}")")")"

# store dockerfile in temp dir
echo "Creating temporary workspace and writing Dockerfile..."
TMP=$(mktemp -d)
trap "{ rm -rf ${TMP}; }" EXIT
cat << EOF > ${TMP}/Dockerfile
FROM python:3.7-alpine

COPY src src
COPY poetry.lock .
COPY pyproject.toml .

RUN pip install poetry==1.0.0a4 && \
    poetry build -f wheel && \
    poetry export -f requirements.txt && \
    pip wheel -w wheelhouse -r requirements.txt && \
    mv dist/* wheelhouse
EOF

# build image, run container, and copy wheelhouse to project root on host
echo "Building image..."
docker build -f ${TMP}/Dockerfile -t 'wheelhouse_builder' ${PROJECT_DIR}
echo "Running container..."
docker run --cidfile ${TMP}/wheelhouse.cid 'wheelhouse_builder'
echo "Cleaning up former wheelhouse and copying over new one from container..."
rm -fr ${PROJECT_DIR}/wheelhouse
docker cp $(cat ${TMP}/wheelhouse.cid):/wheelhouse ${PROJECT_DIR}/wheelhouse
echo "Done."
