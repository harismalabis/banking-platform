FROM rust:1.70

WORKDIR /usr/src/payments

COPY . .

RUN cargo build --release

CMD ["./target/release/payments"]