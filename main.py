from fastapi import FastAPI
import random
#from base58 import b58encodepi
import binascii
import ecdsa
import hashlib

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/seedGenerate")
async def seedGenerate():
    random.seed()
    seed = random.random()
    return {"seed": seed}

@app.get("/generateKeys")
async def generateKeys():
    private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
    public_key = private_key.get_verifying_key()
    private_key_decode = binascii.hexlify(private_key.to_string()).decode('ascii').upper()
    public_key_decode = binascii.hexlify(public_key.to_string()).decode('ascii').upper()
    keys = {"private_key" : private_key_decode, "public_key" : public_key_decode}
    return keys

@app.get("/publicKeyToAddr")
async def publicKeyToAddr(public_key):
    public_key_encode = binascii.hexlify(public_key.to_string()).encode('ascii').upper()
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(hashlib.sha256(public_key_encode.decode('hex')).digest())
    return base58CheckEncode(0, ripemd160.digest())