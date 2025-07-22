FROM rust:1.70

WORKDIR /usr/src/gateway

COPY . .

RUN cargo build --release

CMD ["./target/release/gateway"]