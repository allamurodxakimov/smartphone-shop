from tinydb import TinyDB, Query
from typing import Union

tindb = TinyDB('db.json', indent = 4)
cart = TinyDB('cart.json', indent = 4)
item = cart.table('item')
q = Query()

def get_brends():
    brends = tindb.tables()
    return brends

def get_phones_by_brend(brend: str):
    if brend in get_brends():
        collection = tindb.table(brend)
        return collection.all()
    else:
        return []

def get_phone_by_id(brend: str, doc_id: Union[int, str]):
    if brend in get_brends():
        collection = tindb.table(brend)
        phone = collection.get(doc_id = doc_id)
        return phone

def add_item(user_id: Union[int,str], brend: str, phone_id: Union[str,int]):
    item.insert({
        "user_id": user_id,
        "brend": brend,
        "phone_id": phone_id
    })


def get_items(user_id: Union[int,str]):
    items = item.search(q.user_id == user_id)
    return items

def clear_items(user_id: Union[int,str]):
    items = item.remove(q.user_id == user_id)
    return items
