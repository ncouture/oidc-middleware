#!/bin/bash
#

export _PYTHON=$(python -c 'import sys; print(f"python{sys.version_info.major}.{sys.version_info.minor}")')
export VIRTUAL_ENV

bazel build firestore_middleware:app
