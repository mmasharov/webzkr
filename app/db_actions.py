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

def getZkrInfo(db: str, zkr_id: int):
    """Получение информации о пакете заявок"""
    with UseMyDatabase(db) as cursor:
        _SQL = """SELECT guid_fk, type, nom_zr, date_zr, kod_ubp_pay, name_ubp_pay, ls_ubp_pay, inn_ubp, kpp_ubp, glava_grs, name_ubp_grs, name_bud,
                name_fo, okpo_fo, kod_tofk, name_tofk, date_isp, guid_sv, nom_bo, kod_isp, pr_isp, faip_code, sum_v, kod_v, sum_doc, type_ap,
                order_pl, vid_pl, purpose, kod_income, name_rcp, inn_rcp, kpp_rcp, ls_ubp_rcp, bs_rcp, name_bic_rcp, bic_rcp, ks_bic_rcp, paystatus,
                kdoh, okato, osn_pl, nal_per, nom_dok, date_doc, type_pl, id_pp, period_pay, jnt_ls, id_zhku, dol_ruk_ubp, name_ruk_ubp, dol_buh_ubp, name_buh_ubp,
                date_pod_ubp, nom_zr_fk, date_fk, dol_isp_fk, name_isp_fk, tel_isp_fk, nom_register, id_doc, vid_reestr, osn_plat, vid_osn, nom_osn, date_osn, osn
                FROM zkr
                WHERE zkr_id == ?"""
        cursor.execute(_SQL, (zkr_id,))
        data = cursor.fetchall()

    zkrdata = {}
    for item in data:
        zkrdata['zr-guid_fk'] = item[0]
        zkrdata['zr-type'] = item[1]
        zkrdata['zr-nom_zr'] = item[2]
        zkrdata['zr-date_zr'] = item[3]
        zkrdata['zr-kod_ubp_pay'] = item[4]
        zkrdata['zr-name_ubp_pay'] = item[5]
        zkrdata['zr-ls_ubp_pay'] = item[6]
        zkrdata['zr-inn_ubp'] = item[7]
        zkrdata['zr-kpp_ubp'] = item[8]
        zkrdata['zr-glava_grs'] = item[9]
        zkrdata['zr-name_ubp_grs'] = item[10]
        zkrdata['zr-name_bud'] = item[11]
        zkrdata['zr-name_fo'] = item[12]
        zkrdata['zr-okpo_fo'] = item[13]
        zkrdata['zr-kod_tofk'] = item[14]
        zkrdata['zr-name_tofk'] = item[15]
        zkrdata['zr-date_isp'] = item[16]
        zkrdata['zr-guid_sv'] = item[17]
        zkrdata['zr-nom_bo'] = item[18]
        zkrdata['zr-kod_isp'] = item[19]
        zkrdata['zr-pr_isp'] = item[20]
        zkrdata['zr-faip_code'] = item[21]
        zkrdata['zr-sum_v'] = item[22]
        zkrdata['zr-kod_v'] = item[23]
        zkrdata['zr-sum_doc'] = item[24]
        zkrdata['zr-type_ap'] = item[25]
        zkrdata['zr-order_pl'] = item[26]
        zkrdata['zr-vid_pl'] = item[27]
        zkrdata['zr-purpose'] = item[28]
        zkrdata['zr-kod_income'] = item[29]
        zkrdata['zr-name_rcp'] = item[30]
        zkrdata['zr-inn_rcp'] = item[31]
        zkrdata['zr-kpp_rcp'] = item[32]
        zkrdata['zr-ls_ubp_rcp'] = item[33]
        zkrdata['zr-bs_rcp'] = item[34]
        zkrdata['zr-name_bic_rcp'] = item[35]
        zkrdata['zr-bic_rcp'] = item[36]
        zkrdata['zr-ks_bic_rcp'] = item[37]
        zkrdata['zr-paystatus'] = item[38]
        zkrdata['zr-kdoh'] = item[39]
        zkrdata['zr-okato'] = item[40]
        zkrdata['zr-osn_pl'] = item[41]
        zkrdata['zr-nal_per'] = item[42]
        zkrdata['zr-nom_dok'] = item[43]
        zkrdata['zr-date_dok'] = item[44]
        zkrdata['zr-type_pl'] = item[45]
        zkrdata['zr-id_pp'] = item[46]
        zkrdata['zr-period_pay'] = item[47]
        zkrdata['zr-jnt_ls'] = item[48]
        zkrdata['zr-id_zhku'] = item[49]
        zkrdata['zr-dol_ruk_ubp'] = item[50]
        zkrdata['zr-name_ruk_ubp'] = item[51]
        zkrdata['zr-dol_buh_ubp'] = item[52]
        zkrdata['zr-name_buh_ubp'] = item[53]
        zkrdata['zr-date_pod_ubp'] = item[54]
        zkrdata['zr-nom_zr_fk'] = item[55]
        zkrdata['zr-date_fk'] = item[56]
        zkrdata['zr-dol_isp_fk'] = item[57]
        zkrdata['zr-name_isp_fk'] = item[58]
        zkrdata['zr-tel_isp_fk'] = item[59]
        zkrdata['zrcontr-nom_register'] = item[60]
        zkrdata['zrcontr-id_doc'] = item[61]
        zkrdata['zrcontr-vid_reestr'] = item[62]
        zkrdata['zrosn-osn_plat'] = item[63]
        zkrdata['zrosn-vid_osn'] = item[64]
        zkrdata['zrosn-nom_osn'] = item[65]
        zkrdata['zrosn-date_osn'] = item[66]
        zkrdata['zrosn-osn'] = item[67]

    return zkrdata
        

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

def getStrInfo(db: str, str_id: int):
    """"Получение информации о строке звявки"""
    with UseMyDatabase(db) as cursor:
        _SQL = """SELECT kod_ist_kbk, type_kbk_pay, kbk_pay, type_kbk_rcp, kbk_rcp, add_klass_pay, add_klass_rcp, sum_v_kbk, sum_r_kbk, purpose_kbk, note_kbk
                FROM zrst
                WHERE zrst_id = ?"""
        cursor.execute(_SQL, (str_id,))
        data = cursor.fetchall()
    
    strdata = {}
    for item in data:
        strdata['zrst-kod_ist_kbk'] = item[0]
        strdata['zrst-type_kbk_pay'] = item[1]
        strdata['zrst-kbk_pay'] = item[2]
        strdata['zrst-type_kbk_rcp'] = item[3]
        strdata['zrst-kbk_rcp'] = item[4]
        strdata['zrst-add_klass_pay'] = item[5]
        strdata['zrst-add_klass_rcp'] = item[6]
        strdata['zrst-sum_v_kbk'] = item[7]
        strdata['zrst-sum_r_kbk'] = item[8]
        strdata['zrst-purpose_kbk'] = item[9]
        strdata['zrst-note_kbk'] = item[10]

    return strdata

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