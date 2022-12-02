
# from django.shortcuts import render
# # OP.GG 웹크롤링 라이브러리
# from selenium import webdriver
# from bs4 import BeautifulSoup
# from selenium.webdriver.common.by import By
# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')

# # 크롤링
# path = "./chromedriver.exe"
# driver = webdriver.Chrome(path, chrome_options=options)
# # 3초 타이머
# driver.implicitly_wait(3)
# # OP.GG 챔피언 정보 페이지 주소
# driver.get('https://www.op.gg/champions?region=tr')
# # 페이지의 요소
# html = driver.page_source
# # 페이지 요소 요청하기
# soup = BeautifulSoup(html, 'html.parser')
# # 챔피언 이름
# name = soup.select('#content-container > div.css-1fcwcq0.e2v0byd0 > aside > nav > ul > li > a > span')
# # 챔피언 이미지
# imgs = driver.find_elements(By.CSS_SELECTOR, '#content-container > div.css-1fcwcq0.e2v0byd0 > aside > nav > ul > li > a > img')
# # 챔피언 디테일 페이지 주소
# details = driver.find_elements(By.CSS_SELECTOR, '#content-container > div.css-1fcwcq0.e2v0byd0 > aside > nav > ul > li > a')


# # 챔피언 이름 담을 리스트
# c_name = []
# # 챔피언 이미지 담을 리스트
# c_img = []
# # 챔피언 디테일 주소 담을 리스트
# c_detail = []

# # 크롤링한 챔피언 이름 리스트에 저장
# for n in name:
#     c_name.append(n.text.strip())

# # 이미지 없는 챔피언 이름 리스트에서 삭제
# c_name.remove('아이번')
# c_name.remove('스카너')

# # 크롤링한 이미지 주소 리스트에 저장
# for i in imgs:
#     c_img.append(i.get_attribute('src'))

# # 크롤링한 디테일 주소 리스트에 저장
# for d in details:
#   c_detail.append(d.get_attribute('href'))

# # 이미지 없는 챔피언 주소 리스트에서 삭제
# c_detail.remove('https://www.op.gg/champions/ivern?region=tr&tier=platinum_plus')
# c_detail.remove('https://www.op.gg/champions/skarner?region=tr&tier=platinum_plus')

# # 챔피언 정보 딕셔너리로 저장
# champs = []
# for i in range(len(c_name)):
#   champs.append(
#     {
#       'name' : c_name[i],
#       'img' : c_img[i],
#       'detail' : c_detail[i]
#     }
#   )

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


# # Create your views here.
# def index(request):


#     # for champ in champs:
#     #     name = champ['name']
#     #     img = champ['img']

#     context = {
#         # 'name' : name,
#         # 'img' : img,
#         'champs' : champs,
#     }
#     return render(request, 'champions/index.html', context)

# def detail(request, c_name):
#     for champ in champs:
#         detail = champ['detail']

#     context = {
#         'detail' : detail,
#     }
#     return render(request, 'champions/detail.html', context)
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

