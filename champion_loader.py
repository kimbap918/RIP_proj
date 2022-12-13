import json
import os
from pprint import pprint

BASE_DIR = "static/crawling/json/"
# 챔피언 디테일 정보
with open(os.path.join(BASE_DIR, "champ_detail.json"), "r", encoding="UTF-8") as champs:
    champs = json.load(champs)

new_list = []
for champ in champs:
    new_data = {"model":"champions.champ"}
    new_data["fields"] = {}
    new_data["fields"] = champ
    new_list.append(new_data)
    
print(new_list)
with open(os.path.join(BASE_DIR, "champ_modeling.json"),"w", encoding="UTF-8") as f:
    json.dump(new_list,f,ensure_ascii=False, indent=2)