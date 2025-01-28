FROM python:3.12-slim-bookworm
LABEL authors="Manuel Palmero"

WORKDIR /app

RUN apt-get update &&  \
    apt-get install -y apt-utils && \
    apt-get install -y beep && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app/

ENTRYPOINT ["/bin/bash -c"]

CMD ["python","main.py"]