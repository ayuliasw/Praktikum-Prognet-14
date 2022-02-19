#!/usr/bin/env python3

from Crypto.Util.number import bytes_to_long as b2l, getPrime

message = "{REDACTED}"

class RSA():
    def __init__(self, message, prime_bits):
        self.e = 3
        self.p = getPrime(prime_bits)
        self.q = getPrime(int(prime_bits ** (1/2)))
        self.n = self.p * self.q
        self.message = message
    def encrypt(self):
        message_to_long = b2l((self.message).encode())
        self.c = pow(message_to_long, self.e, self.n)
        return (f"N = {self.n}\ne = {self.e}\nc = {self.c}")

## Find this
find_this = RSA(message, 512)
with open ("./file.enc", "w") as f:
    f.write(find_this.encrypt())
