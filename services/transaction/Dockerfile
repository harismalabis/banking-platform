FROM rust:1.70

WORKDIR /usr/src/transactions

COPY . .

RUN cargo build --release

CMD ["./target/release/transactions"]