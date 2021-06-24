from schema import tables, metadata
from config import engine
from pywallet import wallet
from sqlalchemy import Table, String, Column, Integer, Computed
import helpers

class UserWallet():
    parent_wallet_tbl = tables.parent_wallet
    children_wallet_tbl = tables.children_wallet
    seed = 'nose shallow wheat faculty ill fever pole tube spoon stable sleep mango'

    #Генерим родительский кошелек, seed, а так же 10 дочерних кошельков и все к ним необходимое, сохраняем в бд
    def FirstCreateWallet(self):
        seed = wallet.generate_mnemonic()
        w = wallet.create_wallet(network="BTC", seed=seed, children=10)
        with engine.connect() as conn:
            #запишем пораметры родительского кошелька
            query = self.parent_wallet_tbl.insert().values(
                address = w.get('address'),
                coin = w.get('coin'),
                private_key = w.get('private_key'),
                public_key = w.get('public_key'),
                seed = w.get('seed'),
                wif = w.get('wif'),
                xprivate_key=w.get('xprivate_key'),
                xpublic_key=w.get('xpublic_key'),
                xpublic_key_prime=w.get('xpublic_key_prime')
            )
            conn.execute(query)
            #запишем его детей
            for i in w.get('children'):
                query = self.children_wallet_tbl.insert().values(
                    parent_address = w.get('address'),
                    xpublic_key = i.get('xpublic_key'),
                    address = i.get('address'),
                    path = i.get('path'),
                    bip32_path = i.get('bip32_path')
                )
                conn.execute(query)

    #добавляем дочерний кошелек, на вход принимается xpublic_key родительского кошелька
    @staticmethod
    def CreateChildWallet(xpublic_key):
        rand_addr = wallet.create_address(network="BTC", xpub=xpublic_key)
        return rand_addr

    #находит родитеський кошелек и все его дочерние кошельки по seed фразе
    def FindWalletBySeed(self, seed):
        with engine.connect() as conn:
            #найдем родительский кошелек
            query = self.parent_wallet_tbl.select().where(self.parent_wallet_tbl.c.seed == seed)
            data = conn.execute(query).fetchmany()
            #normal_data = helpers.RowProxyToDict(data)
            return(data)


