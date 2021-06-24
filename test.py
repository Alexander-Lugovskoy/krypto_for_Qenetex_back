from bitcoinaddress import Wallet

wallet = Wallet()
obj = wallet.key
#print(type(obj))
#print(obj)

print(wallet.key.__dict__['hex'])
print(wallet.key.__dict__['mainnet'].__dict__)
print(wallet.key.__dict__['testnet'].__dict__)
print(wallet.address.__dict__)
print(wallet.address.__dict__['mainnet'].__dict__)
print(wallet.address.__dict__['testnet'].__dict__)