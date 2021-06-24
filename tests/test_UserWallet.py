from models import UserWallet
import pprint

"""
count = 0
obj = UserWallet.UserWallet()
while count != 1000:
    obj.FirstCreateWallet()
    print("count: ", count)
    count +=1
"""

"""
count = 0
obj = UserWallet.UserWallet()
while count != 10:
    xpublic_key = 'xpub661MyMwAqRbcFrr8MMYfSwJTZTZB3qtGEnBxeyuKRGw3K27FWzQNYeT6fJ42MegYRYUusekfJGLdXG4CFhchcjrF2GRREuizzy7w5DgmuUZ'
    test = obj.CreateChildWallet(xpublic_key)
    pprint.pprint(test)
    print("count: ", count)
    count +=1
"""

obj = UserWallet.UserWallet()
seed = 'nose shallow wheat faculty ill fever pole tube spoon stable sleep mango'
result = obj.FindWalletBySeed(seed)
print(result)