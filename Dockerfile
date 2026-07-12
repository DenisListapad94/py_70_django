FROM python:3.11-alpine

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app/src

# RUN apk add --no-cache \
#     postgresql-client \
#     libjpeg-turbo \
#     zlib \
#     && apk add --no-cache --virtual .build-deps \
#     gcc \
#     musl-dev \
#     libc-dev \
#     linux-headers \
#     postgresql-dev \
#     jpeg-dev \
#     zlib-dev


WORKDIR app
COPY requirements.txt .
RUN pip install  -r requirements.txt


COPY src/ src/
COPY static/ static/
COPY templates/ templates/
COPY .env .env


RUN chmod +x src/scripts/entrypoint.dev.sh
CMD ["sh", "src/scripts/entrypoint.dev.sh"]

