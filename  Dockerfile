# ---------- Build stage -------------------------------------------------------
FROM python:3.11-slim AS builder

# Install build tools & create virtual env inside image
RUN apt-get update && apt-get install -y --no-install-recommends build-essential gcc && \
    python -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Copy lockfile & install exactly-pinned deps
COPY requirements.lock .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.lock

# Copy project source
COPY src/ ./src/

# ---------- Runtime stage -----------------------------------------------------
FROM python:3.11-slim

ENV PATH="/opt/venv/bin:$PATH" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY --from=builder /opt/venv /opt/venv
COPY src/ ./src/

CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-w", "4", "-b", "0.0.0.0:8080", "calendar_agent.api.v1:app"]