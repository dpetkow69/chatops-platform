FROM python:3.12-slim AS builder
WORKDIR /build
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

FROM python:3.12-slim
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*
RUN useradd -r -u 1001 -s /bin/false chatops
WORKDIR /app
COPY --from=builder /root/.local /home/chatops/.local
COPY --chown=chatops:chatops . .
USER chatops
ENV PATH=/home/chatops/.local/bin:$PATH
HEALTHCHECK --interval=15s --timeout=5s --start-period=20s --retries=3 \
  CMD curl -sf http://localhost:8002/health || exit 1
EXPOSE 8002
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002"]
