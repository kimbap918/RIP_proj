from django.shortcuts import render

# OP.GG 웹크롤링 json 파일
import json
import os

BASE_DIR = "static/crawling/json/"

# 챔피언 이름 / 챔피언 이미지 / 디테일 주소
with open(os.path.join(BASE_DIR, "infos.json"), "r", encoding="UTF-8") as infos:
    infos = json.load(infos)
# 탑 랭킹 정보
with open(os.path.join(BASE_DIR, "top.json"), "r", encoding="UTF-8") as top:
    top = json.load(top)
# 정글 랭킹 정보
with open(os.path.join(BASE_DIR, "jungle.json"), "r", encoding="UTF-8") as jungle:
    jungle = json.load(jungle)
# 미드 랭킹 정보
with open(os.path.join(BASE_DIR, "mid.json"), "r", encoding="UTF-8") as mid:
    mid = json.load(mid)
# 바텀 랭킹 정보
with open(os.path.join(BASE_DIR, "adc.json"), "r", encoding="UTF-8") as adc:
    adc = json.load(adc)
# 서포터 랭킹 정보
with open(os.path.join(BASE_DIR, "support.json"), "r", encoding="UTF-8") as support:
    support = json.load(support)
# 챔피언 디테일 정보
with open(os.path.join(BASE_DIR, "champ_detail.json"), "r", encoding="UTF-8") as champs:
    champs = json.load(champs)
# Create your views here.
def index(request):

    context = {
        "infos": infos,
        "top": top,
        "jungle": jungle,
        "mid": mid,
        "adc": adc,
        "support": support,
    }
    return render(request, "champions/index.html", context)


def detail(request, name):

    detail = {}
    info_d = []  # 승률, 픽률, 밴률, 티어

    for champ in champs:
        if champ["name"] == name:
            detail["name"] = champ["name"]
            detail["lane"] = champ["lane"]
            detail["skill"] = champ["skill"]
            detail["skilltree"] = champ["skilltree"]
            detail["skilltrees"] = champ["skilltrees"]
            detail["skillpick"] = champ["skillpick"]
            detail["skillwin"] = champ["skillwin"]
            detail["s_item1"] = champ["s_item1"]
            detail["s_itempick1"] = champ["s_itempick1"]
            detail["s_itemwin1"] = champ["s_itemwin1"]
            detail["s_item2"] = champ["s_item2"]
            detail["s_itempick2"] = champ["s_itempick2"]
            detail["s_itemwin2"] = champ["s_itemwin2"]
            detail["s_shoe1"] = champ["s_shoe1"]
            detail["s_shoepick1"] = champ["s_shoepick1"]
            detail["s_shoewin1"] = champ["s_shoewin1"]
            detail["s_shoe2"] = champ["s_shoe2"]
            detail["s_shoepick2"] = champ["s_shoepick2"]
            detail["s_shoewin2"] = champ["s_shoewin2"]
            detail["item1"] = champ["item1"]
            detail["itempick1"] = champ["itempick1"]
            detail["itemwin1"] = champ["itemwin1"]
            detail["item2"] = champ["item2"]
            detail["itempick2"] = champ["itempick2"]
            detail["itemwin2"] = champ["itemwin2"]
            detail["item3"] = champ["item3"]
            detail["itempick3"] = champ["itempick3"]
            detail["itemwin3"] = champ["itemwin3"]
            detail["item4"] = champ["item4"]
            detail["itempick4"] = champ["itempick4"]
            detail["itemwin4"] = champ["itemwin4"]
            detail["item5"] = champ["item5"]
            detail["itempick5"] = champ["itempick5"]
            detail["itemwin5"] = champ["itemwin5"]
            detail["hard_img"] = champ["hard_img"]
            detail["hard_win"] = champ["hard_win"]
            detail["easy_img"] = champ["easy_img"]
            detail["easy_win"] = champ["easy_win"]
            detail["rune_j"] = champ["rune_j"]
            detail["rune_js"] = champ["rune_js"]
            detail["rune_j_name"] = champ["rune_j_name"]
            detail["rune_k"] = champ["rune_k"]
            detail["rune_ks"] = champ["rune_ks"]
            detail["rune_k_name"] = champ["rune_k_name"]
            detail["rune_n"] = champ["rune_n"]
            detail["rune_n_name"] = champ["rune_n_name"]
            detail["rune_img1"] = champ["rune_img1"]
            detail["rune_pick1"] = champ["rune_pick1"]
            detail["rune_win1"] = champ["rune_win1"]
            detail["rune_img2"] = champ["rune_img2"]
            detail["rune_pick2"] = champ["rune_pick2"]
            detail["rune_win2"] = champ["rune_win2"]

    for t in top:
        if t["name"] == name:
            info_d.append(t["win"])
            info_d.append(t["pick"])
            info_d.append(t["ben"])
            info_d.append(t["tier"])
    for t in jungle:
        if t["name"] == name:
            info_d.append(t["win"])
            info_d.append(t["pick"])
            info_d.append(t["ben"])
            info_d.append(t["tier"])
    for t in mid:
        if t["name"] == name:
            info_d.append(t["win"])
            info_d.append(t["pick"])
            info_d.append(t["ben"])
            info_d.append(t["tier"])
    for t in adc:
        if t["name"] == name:
            info_d.append(t["win"])
            info_d.append(t["pick"])
            info_d.append(t["ben"])
            info_d.append(t["tier"])
    for t in support:
        if t["name"] == name:
            info_d.append(t["win"])
            info_d.append(t["pick"])
            info_d.append(t["ben"])
            info_d.append(t["tier"])
    context = {
        "detail": detail,
        "info": info_d,
        "champs": champs,
        "name": name,
    }
    return render(request, "champions/detail.html", context)
