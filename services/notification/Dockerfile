FROM rust:1.70

WORKDIR /usr/src/notifications

COPY . .

RUN cargo build --release

CMD ["./target/release/notifications"]