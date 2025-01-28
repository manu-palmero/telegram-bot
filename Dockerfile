FROM python:3.12-bookworm
LABEL authors="Manuel Palmero"

WORKDIR /app
COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt > /dev/null

COPY . /app/

CMD ["python", "main.py"]