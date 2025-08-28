FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

# Install system dependencies required for cffi and cryptography
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /code/
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

COPY . /code/

CMD ["daphne", "social_network.wsgi:application", "--bind", "0.0.0.0:8000"]
