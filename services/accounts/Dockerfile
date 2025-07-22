# Stage 1: Build environment
FROM python:3.11-slim as builder

WORKDIR /app

# Install system deps + pip packages
RUN apt-get update && apt-get install -y gcc

COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Stage 2: Final runtime image
FROM python:3.11-slim

WORKDIR /app

# Copy app code
COPY . .

# Copy installed packages from builder
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

EXPOSE 5000

CMD ["python", "app.py"]
