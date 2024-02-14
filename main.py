from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from app.dropdown_element import getDropdownElements
from app.db_actions import getZkrPackList, getZkrList, getZkrStrList, getZkrPack, insertZkrPack, getZkrInfo

origins = ["http://localhost", "http://localhost:4000"]
db_path = 'assets\\zkr.db'

myapi = FastAPI()
myapi.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@myapi.get('/zkr_pack/')
def showZkrPackList():
    """Отображение списка пакетов заявок на кассовый расход"""
    return getZkrPackList(db_path)

@myapi.post('/zkr_pack/')
def writeZkrPack(data = Body()):
    """Запись в базу данных информации о новом пакете ЗКР"""
    insertZkrPack(db_path, data)


@myapi.get('/zkr_pack/{pack_id}')
def showZkrPack(pack_id):
    """Заполнение блока информации о пакете ЗКР"""
    return getZkrPack(db_path, pack_id)

@myapi.get('/zkr/{parent_id}')
def showZkrList(parent_id):
    """Отображение списка заявок в пакете"""
    return getZkrList(db_path, parent_id)

@myapi.get('/zkr_info/{zkr_id}')
def showZkrInfo(zkr_id):
    """Заполнение блока информации о заявке"""
    return getZkrInfo(db_path, zkr_id)

@myapi.get('/zrst/{parent_id}')
def showZrstList(parent_id):
    """Отображение списка строк заявки"""
    return getZkrStrList(db_path, parent_id)

@myapi.get('/budg_level/')
def getBudgLevels():
    """Выпадающий список уровней бюджета"""
    return getDropdownElements(db_path, 'budg_level')

@myapi.get('/level/')
def getSecureLevels():
    """Выпадающий список уровней конфиденциальности"""
    return getDropdownElements(db_path, 'secure_level')

@myapi.get('/type/')
def getZrType():
    """Выпадающий список типа заявки"""
    return getDropdownElements(db_path, 'zr_type')

@myapi.get('/type_ap/')
def getApType():
    """Выпадающий список признака авансового платежа"""
    return getDropdownElements(db_path, 'type_ap')

@myapi.get('/vid_pl/')
def getVidPl():
    """Выпадающий список вида платежа"""
    return getDropdownElements(db_path, 'vid_pl')

@myapi.get('/kod_income/')
def getKodIncome():
    """Выпадающий список кода вида дохода"""
    return getDropdownElements(db_path, 'kod_income')

@myapi.get('/osn_plat/')
def getOsnPlat():
    """Выпадающий список оснований платежа"""
    return getDropdownElements(db_path, 'osn_plat')

@myapi.get('/kod_ist_kbk/')
def getKodIstKbk():
    """Выпадающий список источника средств"""
    return getDropdownElements(db_path, 'kod_ist_kbk')

@myapi.get('/type_kbk_pay/')
@myapi.get('/type_kbk_rcp/')
def getTypeKbkPay():
    """Выпадающий список типов КБК"""
    return getDropdownElements(db_path, 'type_kbk')