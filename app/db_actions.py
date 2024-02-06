from app.dbconn import UseMyDatabase
import json

def getZkrPackList(db):
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

def getZkrList(db, parent_id):
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

def getZkrStrList(db, parent_id):
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