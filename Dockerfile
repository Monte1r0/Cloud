FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY leakcheck.py .

ENTRYPOINT ["python", "leakcheck.py"]
