FROM vault:latest

# Optional: Add configs or scripts here
COPY config.hcl /vault/config/config.hcl

CMD ["vault", "server", "-config=/vault/config/config.hcl"]