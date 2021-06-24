from sqlalchemy import Table, String, Column, Integer, Computed, MetaData, ForeignKey
#from schema import metadata

metadata = MetaData()

parent_wallet = Table (
    "parent_wallet",
    metadata,
    Column('address', String(34), nullable=False, unique=True, primary_key=True),
    Column('coin', String(5), nullable=False),
    Column('private_key', String(64), nullable=False, unique=True),
    Column('public_key', String(130), nullable=False, unique=True),
    Column('seed', String(130), nullable=False, unique=True),
    Column('wif', String(130), nullable=False, unique=True),
    Column('xprivate_key', String(111), nullable=False, unique=True),
    Column('xpublic_key', String(111), nullable=False, unique=True),
    Column('xpublic_key_prime', String(111), nullable=False, unique=True)
)

children_wallet = Table (
    "children_wallet",
    metadata,
    Column('parent_address', String(34), ForeignKey('parent_wallet.address'), nullable=False),
    Column('address', String(34), nullable=False, unique=True),
    Column('bip32_path', String(20), nullable=False),
    Column('path', String(10), nullable=False),
    Column('xpublic_key', String(111), nullable=False, unique=True)
)