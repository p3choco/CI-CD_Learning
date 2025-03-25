FROM python:3.9-slim

# Ustaw katalog roboczy
WORKDIR /app

# Skopiuj plik z zależnościami i zainstaluj je
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# Skopiuj kod źródłowy
COPY src/ /app/src

# Otwórz port 5000 na potrzeby kontenera
EXPOSE 5000

# Domyślne polecenie uruchamiające aplikację
CMD ["python", "/app/src/app.py"]
