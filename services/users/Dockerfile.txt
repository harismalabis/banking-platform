FROM rust:1.70

WORKDIR /usr/src/users

COPY . .

RUN cargo build --release

CMD ["./target/release/users"]