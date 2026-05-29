FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY web_app.py .
COPY app/ app/
COPY static/ static/

# Папка data монтируется через внешний volume (данные сохраняются между деплоями)
VOLUME ["/app/data"]

RUN mkdir -p data \
    && addgroup --system appgroup \
    && adduser --system --ingroup appgroup appuser \
    && chown -R appuser:appgroup /app

USER appuser

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=10s --start-period=15s --retries=3 \
    CMD python -c "import socket; s=socket.create_connection(('localhost',8000),timeout=5); s.close()" || exit 1

CMD ["python", "web_app.py"]
