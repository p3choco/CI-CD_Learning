FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ /app/src

ENV FLASK_ENV=production

EXPOSE 5000
CMD ["python", "/app/src/app.py"]
