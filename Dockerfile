FROM python:3.12-slim-bookworm
LABEL authors="Manuel Palmero"

WORKDIR /app

RUN apt-get update &&  \
    apt-get upgrade -y && \
    apt-get install -y apt-utils && \
    apt-get install -y beep && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY . /app/

RUN python -m pip install -U pip

RUN python -m pip install .

CMD ["python","main.py"]