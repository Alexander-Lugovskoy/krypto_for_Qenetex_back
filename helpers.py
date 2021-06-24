#преобразуем sqlalchemy.engine.result.RowProxy объект (результат выборки из бд) в говна какого то в словарь
def RowProxyToDict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))

    return d
#_asdict()
def RowProxyToDictV2(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))

    return d