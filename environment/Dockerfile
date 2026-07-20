FROM python:3.13-slim-bookworm@sha256:dd86541a59b252667f4c12f8b2ee17216de37dd65ac773bf097bef996fa78860

RUN pip install --no-cache-dir pytest==8.4.1 pytest-json-ctrf==0.3.5

WORKDIR /app

COPY access.log /app/access.log
