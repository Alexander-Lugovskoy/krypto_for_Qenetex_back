import hashlib
import ecdsa
import os
from binascii import hexlify
from base58 import b58encode


# Installation:
#     pip install base58 ecdsa

# Use that service to make sure that this generator works well:
#   1. navigate to https://bitcoinpaperwallet.com/bitcoinpaperwallet/generate-wallet.html#
#   2. Press "Skip"
#   3. Press "Enter my own key, ..."
#   4. Enter generated private key
#   5. Press "Apply"
#   6. Make sure that everything matches! PROFIT!


def random_secret_exponent(curve_order):
    while True:
        bytes = os.urandom(32)
        random_hex = hexlify(bytes)
        random_int = int(random_hex, 16)
        if random_int >= 1 and random_int < curve_order:
            return random_int


def generate_private_key():
    curve = ecdsa.curves.SECP256k1
    se = random_secret_exponent(curve.order)
    from_secret_exponent = ecdsa.keys.SigningKey.from_secret_exponent
    return from_secret_exponent(se, curve, hashlib.sha256).to_string()


def get_public_key_uncompressed(private_key_bytes):
    k = ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1)
    return b'\04' + k.get_verifying_key().to_string()  # 0x04 = uncompressed key prefix


def get_bitcoin_address(public_key_bytes, prefix=b'\x00'):
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(hashlib.sha256(public_key_bytes).digest())
    r = prefix + ripemd160.digest()
    checksum = hashlib.sha256(hashlib.sha256(r).digest()).digest()[0:4]
    return b58encode(r + checksum)


def main():
    # private_key = generate_private_key()

    #     or:

    private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1).to_string()

    public_key = get_public_key_uncompressed(private_key)
    public_key2 = get_public_key_uncompressed(private_key)

    address = get_bitcoin_address(public_key)
    address2 = get_bitcoin_address(public_key)


    print(f'private key: {hexlify(private_key)}')
    print(f'public key uncompressed: {hexlify(public_key)}')
    print(f'public key uncompressed: {hexlify(public_key2)}')
    print(f'btc address: {address}')
    print(f'btc address2: {address2}')


if __name__ == '__main__':
    main()