import json
import os

BASE_DIR = "static/crawling/json/"

# with open('static\crawling\json\infos.json', 'r') as f:
#     infos = json.load(f, encoding='cp949')


with open(
    os.path.join(BASE_DIR, "infos.json"), "r", encoding="UTF-8"
) as infos:
    infos = json.load(infos)
