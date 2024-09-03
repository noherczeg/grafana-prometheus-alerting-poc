# Dockerfile for the Telemetry Data Generator
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY telemetry_generator.py .

CMD ["python", "telemetry_generator.py"]
