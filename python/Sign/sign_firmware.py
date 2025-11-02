#!/usr/bin/env python3
# sign_firmware.py
# 用法: python sign_firmware.py private.pem firmware.bin signature.bin

import sys
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend

def load_private_key(path, password=None):
    with open(path, "rb") as f:
        data = f.read()
    return serialization.load_pem_private_key(data, password=password, backend=default_backend())

def sign_file(privkey, path, out_sig_path, chunk=1024*1024):
    # 計算 SHA256 digest 並以私鑰簽署 digest (PKCS#1 v1.5)
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    with open(path, "rb") as f:
        while True:
            b = f.read(chunk)
            if not b: break
            digest.update(b)
    digest_val = digest.finalize()
    sig = privkey.sign(
        digest_val,
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    with open(out_sig_path, "wb") as s:
        s.write(sig)
    return len(sig)

def main():
    if len(sys.argv) != 4:
        print("Usage: python sign_firmware.py <private.pem> <firmware.bin> <signature.bin>", file=sys.stderr)
        sys.exit(2)
    priv_path, fw_path, sig_path = sys.argv[1:4]
    privkey = load_private_key(priv_path)
    size = sign_file(privkey, fw_path, sig_path)
    print(f"Signature written ({size} bytes) to {sig_path}")

if __name__ == "__main__":
    main()
