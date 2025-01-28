FROM python:3.12-bookworm
LABEL authors="Manuel Palmero"

WORKDIR /app

RUN apt-get update &&  \
    apt-get install -y apt-utils && \
    apt-get install -y beep && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app/

ENTRYPOINT ["/bin/bash"]

CMD ["python","main.py"]