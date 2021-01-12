#
# This app requires Python 3.7 builtins like `async' and `await'.
#

# Start by building the application.
FROM python:3.7-buster as build

WORKDIR /app
ADD . /app
RUN apt-get update && apt-get install -y --no-install-recommends \
        python3 \
        python3-dev \
        python3-pip \
        python3-wheel \
        python3-setuptools
RUN update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1
RUN pip install -r requirements.txt

RUN flit build

# Now copy it into our base image.
FROM gcr.io/distroless/python3

COPY --from=build /usr/local/lib/python3.7/site-packages /usr/local/lib/python3.7/site-packages/
COPY --from=build /app /
CMD ["/firestore_middlware/app.py"]
