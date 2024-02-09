import json
from app.dbconn import UseMyDatabase

def getZkrPackList(db: str):
    """Получение списка пакетов ЗКР"""
    with UseMyDatabase(db) as cursor:
        _SQL = 'SELECT zkr_pack_id, finished, exported, name_ubp, name_tofk FROM zkr_pack;'
        cursor.execute(_SQL)
        data = cursor.fetchall()

    zkr_list = []
    for item in data:
        result = {}
        result['finished'] = item[1]
        result['exported'] = item[2]
        result['number'] = item[0]
        result['ubp_name'] = item[3]
        result['tofk_name'] = item[4]
        zkr_list.append(result)

    return zkr_list

def getZkrPack(db: str, pack_id: int):
    """Получение информации о пакете заявок"""
    with UseMyDatabase(db) as cursor:
        _SQL = f'SELECT budg_level, kod_ubp, name_ubp, kod_tofk, name_tofk, level, cause FROM zkr_pack WHERE zkr_pack_id == {pack_id}'
        cursor.execute(_SQL)
        data = cursor.fetchall()
    
    packdata = {}
    for item in data:
        packdata['from-budg_level'] = item[0]
        packdata['from-kod_ubp'] = item[1]
        packdata['from-name_ubp'] = item[2]
        packdata['to-kod_tofk'] = item[3]
        packdata['to-name_tofk'] = item[4]
        packdata['secure-level'] = item[5]
        packdata['secure-cause'] = item[6]
    
    return packdata

def getZkrList(db: str, parent_id: int):
    """Получение списка ЗКР в пакете"""
    with UseMyDatabase(db) as cursor:
        _SQL = f'SELECT zkr_id, nom_zr, date_zr, name_ubp_pay, sum_v FROM zkr WHERE parent_id == {parent_id}'
        cursor.execute(_SQL)
        data = cursor.fetchall()

    zkr_list = []
    for item in data:
        result = {}
        result['zkr_id'] = item[0]
        result['nom_pack'] = item[1]
        result['date_zr'] = item[2]
        result['name_ubp_pay'] = item[3]
        result['sum_v'] = item[4]
        zkr_list.append(result)

    return zkr_list

def getZkrStrList(db: str, parent_id: int):
    """Получение строк заявки"""
    with UseMyDatabase(db) as cursor:
        _SQL = f'SELECT zrst_id, parent_id, type_kbk_pay, kbk_pay, sum_v_kbk FROM zrst WHERE parent_id == {parent_id}'
        cursor.execute(_SQL)
        data = cursor.fetchall()
    
    zrst_list = []
    for item in data:
        result = {}
        result['str_id'] = item[0]
        result['nom_zr'] = item[1]
        result['kbk_type'] = item[2]
        result['kbk_pay'] = item[3]
        result['kbk_sum'] = item[4]
        zrst_list.append(result)
    
    return zrst_list

def insertZkrPack(db: str, data_json) -> None:
    """Запись в базу данных информации о новом пакете ЗКР"""
    data = json.loads(data_json)
    with UseMyDatabase(db) as cursor:
        if data['pack_id'] == 0:
            _SQL = """INSERT INTO zkr_pack
                    (format_version, soft_name, soft_version, budg_level, kod_ubp, name_ubp, kod_tofk, name_tofk, level, cause)
                    VALUES
                    ('TXZR220401', 'WebZKR', '1.0', ?, ?, ?, ?, ?, ?, ?)"""
            cursor.execute(_SQL, (data['from-budg_level'], data['from-kod_ubp'], data['from-name_ubp'], data['to-kod_tofk'], data['to-name_tofk'], data['secure-level'], data['secure-cause'],))
        else:
            _SQL = """UPDATE zkr_pack
                SET budg_level = ?,
                    kod_ubp = ?,
                    name_ubp = ?,
                    kod_tofk = ?,
                    name_tofk = ?,
                    level = ?,
                    cause = ?
                WHERE zkr_pack_id == ?"""
            cursor.execute(_SQL, (data['from-budg_level'], data['from-kod_ubp'], data['from-name_ubp'], data['to-kod_tofk'], data['to-name_tofk'], data['secure-level'], data['secure-cause'], data['pack_id'],))