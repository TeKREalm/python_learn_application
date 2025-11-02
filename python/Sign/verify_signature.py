#!/usr/bin/env python3
# verify_signature.py
# 用法: python verify_signature.py public.pem firmware.bin signature.bin

import sys
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend

def load_public_key(path):
    with open(path, "rb") as f:
        data = f.read()
    return serialization.load_pem_public_key(data, backend=default_backend())

def compute_sha256(path, chunk=1024*1024):
    h = hashes.Hash(hashes.SHA256(), backend=default_backend())
    with open(path, "rb") as f:
        while True:
            b = f.read(chunk)
            if not b: break
            h.update(b)
    return h.finalize()

def main():
    if len(sys.argv) != 4:
        print("Usage: python verify_signature.py <public.pem> <firmware.bin> <signature.bin>", file=sys.stderr)
        sys.exit(2)
    pub_path, fw_path, sig_path = sys.argv[1:4]
    pub = load_public_key(pub_path)
    digest = compute_sha256(fw_path)
    sig = open(sig_path, "rb").read()
    try:
        pub.verify(
            sig,
            digest,
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        print("Signature: VALID")
        sys.exit(0)
    except Exception as e:
        print("Signature: INVALID", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
