#light weight image
FROM python:3.9-slim

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt gunicorn

# Expose internal port
EXPOSE 5000

# Run this with Gunicorn (production WSGI server)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
