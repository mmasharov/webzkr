--
-- File generated with SQLiteStudio v3.1.1 on ѕн фев 5 17:48:50 2024
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: budg_level
CREATE TABLE budg_level (budg_level_code INTEGER UNIQUE NOT NULL, budg_level_name TEXT NOT NULL);

-- Table: kod_income
CREATE TABLE kod_income (kod_income_code INTEGER UNIQUE NOT NULL, kod_income_name TEXT NOT NULL);

-- Table: kod_ist_kbk
CREATE TABLE kod_ist_kbk (kod_ist_kbk_code INTEGER UNIQUE NOT NULL, kod_ist_kbk_name TEXT NOT NULL);

-- Table: osn_plat
CREATE TABLE osn_plat (osn_plat_code INTEGER UNIQUE NOT NULL, osn_plat_name TEXT NOT NULL);

-- Table: secure_level
CREATE TABLE secure_level (secure_level_code INTEGER NOT NULL UNIQUE, secure_level_name TEXT NOT NULL);

-- Table: type_ap
CREATE TABLE type_ap (type_ap_code INTEGER UNIQUE NOT NULL, type_ap_name TEXT NOT NULL);

-- Table: type_kbk
CREATE TABLE type_kbk (type_kbk_code INTEGER NOT NULL UNIQUE, type_kbk_name TEXT NOT NULL);

-- Table: vid_pl
CREATE TABLE vid_pl (vid_pl_code INTEGER UNIQUE NOT NULL, vid_pl_name TEXT NOT NULL);

-- Table: vid_reestr
CREATE TABLE vid_reestr (vid_reestr_code INTEGER, vid_reestr_name TEXT);

-- Table: zkr
CREATE TABLE zkr (zkr_id INTEGER PRIMARY KEY, parent_id INTEGER REFERENCES zkr_pack (zkr_pack_id), guid_fk TEXT, type INTEGER REFERENCES zr_type (zr_type_code), nom_zr TEXT, date_zr DATE, kod_ubp_pay TEXT, name_ubp_pay TEXT, ls_ubp_pay TEXT, inn_ubp TEXT, kpp_ubp TEXT, glava_grs TEXT, name_ubp_grs TEXT, name_bud TEXT, name_fo TEXT, okpo_fo TEXT, kod_tofk TEXT, name_tofk TEXT, date_isp DATE, guid_sv TEXT, nom_bo TEXT, kod_isp TEXT, pr_isp TEXT, faip_code TEXT, sum_v REAL, kod_v TEXT, sum_doc REAL, type_ap INTEGER REFERENCES type_ap (type_ap_code), order_pl INTEGER, vid_pl INTEGER REFERENCES vid_pl (vid_pl_code), purpose TEXT, kod_income INTEGER, name_rcp TEXT, inn_rcp TEXT, kpp_rcp TEXT, ls_ubp_rcp TEXT, bs_rcp TEXT, name_bic_rcp TEXT, bic_rcp TEXT, ks_bic_rcp TEXT, paystatus TEXT, kdoh TEXT, okato TEXT, osn_pl TEXT, nal_per TEXT, nom_dok TEXT, date_doc TEXT, type_pl TEXT, id_pp TEXT, period_pay TEXT, jnt_ls TEXT, id_zhku TEXT, dol_ruk_ubp TEXT, name_ruk_ubp TEXT, dol_buh_ubp TEXT, name_buh_ubp TEXT, date_pod_ubp DATE, nom_zr_fk TEXT, date_fk DATE, dol_isp_fk TEXT, name_isp_fk TEXT, tel_isp_fk TEXT, nom_register TEXT, id_doc TEXT, vid_reestr INTEGER, osn_plat INTEGER REFERENCES osn_plat (osn_plat_code), vid_osn TEXT, nom_osn TEXT, date_osn DATE, osn TEXT);

-- Table: zkr_pack
CREATE TABLE zkr_pack (zkr_pack_id INTEGER PRIMARY KEY, finished BOOLEAN NOT NULL DEFAULT (0), exported BOOLEAN NOT NULL DEFAULT (0), format_version TEXT NOT NULL, soft_name TEXT, soft_version TEXT, note TEXT, budg_level INTEGER REFERENCES budg_level (budg_level_code), kod_ubp TEXT, name_ubp TEXT, kod_tofk TEXT, name_tofk TEXT, level INTEGER REFERENCES secure_level (secure_level_code), cause TEXT);

-- Table: zr_type
CREATE TABLE zr_type (zr_type_code INTEGER UNIQUE NOT NULL, zr_type_name TEXT NOT NULL);

-- Table: zrst
CREATE TABLE zrst (zrst_id INTEGER PRIMARY KEY, parent_id INTEGER REFERENCES zkr (zkr_id), kod_ist_kbk INTEGER REFERENCES kod_ist_kbk (kod_ist_kbk_code), type_kbk_pay INTEGER REFERENCES type_kbk (type_kbk_code), kbk_pay TEXT, type_kbk_rcp INTEGER REFERENCES type_kbk (type_kbk_code), kbk_rcp TEXT, add_klass_pay TEXT, add_klass_rcp TEXT, sum_v_kbk REAL, sum_r_kbk REAL, purpose_kbk TEXT, note_kbk TEXT);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
