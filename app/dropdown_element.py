from app.dbconn import UseMyDatabase
import json

def getDropdownElements(db, element):
    """Получение элементов для выпадающего списка"""
    with UseMyDatabase(db) as cursor:
        _SQL = f'SELECT * from {element} ORDER BY {element}_code ASC;'
        cursor.execute(_SQL)
        data = cursor.fetchall()
    result = {}
    for item in data:
        result[item[0]] = item[1]
    
    return json.dumps(result)