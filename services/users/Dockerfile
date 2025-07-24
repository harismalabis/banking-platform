# Stage 1: Builder
FROM python:3.11-slim as builder

WORKDIR /app

# System dependencies
RUN apt-get update && apt-get install -y gcc

# Install Python dependencies
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Copy source code
COPY . .

# Stage 2: Distroless image
FROM gcr.io/distroless/python3-debian11

WORKDIR /app

# Copy installed packages and app code from builder
COPY --from=builder /root/.local /root/.local
COPY --from=builder /app /app

# Set environment path so Python + Uvicorn is accessible
ENV PATH=/root/.local/bin:$PATH

# Port (optional – ignored by distroless)
EXPOSE 5006

# Start Uvicorn server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5006"]