from pywallet import wallet
import pprint
from sqlalchemy import create_engine, Table, String, Column, MetaData, Integer, Computed

import db_connect

# generate 12 word mnemonic seed
seed = wallet.generate_mnemonic()
# create bitcoin wallet
w = wallet.create_wallet(network="BTC", seed=seed, children=10)
#print(w.get('address'))
pprint.pprint(w)
"""
children = w.get('children')
for i in children:
    print(i)
"""
"""
engine = create_engine("postgresql+psycopg2://postgres:aaa914@localhost/krypto_for_Qenetex")
metadata = MetaData()
data = Table(
    "data",
    metadata,
    Column(
        'id', Integer, primary_key=True
    ),
    Column(
        'data', String
    )
    Column(
        'somecolumn', String
    )
)
data.create(engine)
"""
