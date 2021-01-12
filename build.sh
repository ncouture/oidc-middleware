#!/bin/bash
#

echo "========================================================================="
echo "Building docker image firestore_middlewar:app"
echo "========================================================================="
docker build -t app .
bazel build firestore_middleware:app
