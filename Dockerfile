FROM python:3.10-slim-bookworm

WORKDIR /app

COPY . /app

RUN apt-get update -y && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir torch==2.2.1+cpu --index-url https://download.pytorch.org/whl/cpu && \
    sed -i '/torch==2.2.1/d' requirements.txt && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["python3", "app.py"]
