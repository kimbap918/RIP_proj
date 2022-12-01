from django.shortcuts import render
# OP.GG 웹크롤링 json 파일
import json
import os

BASE_DIR = "static/crawling/json/"

# 챔피언 이름 / 챔피언 이미지 / 디테일 주소
with open(
    os.path.join(BASE_DIR, "infos.json"), "r", encoding="UTF-8"
) as infos:
    infos = json.load(infos)
# 탑 랭킹 정보
with open(
    os.path.join(BASE_DIR, "top.json"), "r", encoding="UTF-8"
) as top:
    top = json.load(top)
# 정글 랭킹 정보
with open(
    os.path.join(BASE_DIR, "jungle.json"), "r", encoding="UTF-8"
) as jungle:
    jungle = json.load(jungle)
# 미드 랭킹 정보
with open(
    os.path.join(BASE_DIR, "mid.json"), "r", encoding="UTF-8"
) as mid:
    mid = json.load(mid)
# 바텀 랭킹 정보
with open(
    os.path.join(BASE_DIR, "adc.json"), "r", encoding="UTF-8"
) as adc:
    adc = json.load(adc)
# 서포터 랭킹 정보
with open(
    os.path.join(BASE_DIR, "support.json"), "r", encoding="UTF-8"
) as support:
    support = json.load(support)

# Create your views here.
def index(request):

    context = {
        'infos' : infos,
        'top' : top,
        'jungle' : jungle,
        'mid' : mid,
        'adc' : adc,
        'support' : support,
    }
    return render(request, 'champions/index.html', context)

# def lane_name(request, lane):

#     context = {
#         'lane' : lane,
#     }
#     return render(request, 'champions/index.html', context)

# def detail(request, c_name):
#     for champ in champs:
#         detail = champ['detail']
    
#     context = {
#         'detail' : detail,
#     }
#     return render(request, 'champions/detail.html', context)