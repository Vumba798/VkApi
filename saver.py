import json

from User import *

def getJson(data) -> str:
    return json.dumps(data, ensure_ascii=False, sort_keys=True, indent=4)

def save_to_file(data, filename: str, append: bool = True):
    with open("saved/" + filename, "w", encoding="utf-8") as file:
        file.write(getJson(data))