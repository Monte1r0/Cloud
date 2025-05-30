FROM python:3.10-slim

WORKDIR /app

COPY check_leak.py ./

RUN pip install requests beautifulsoup4

CMD ["python", "check_leak.py"]
