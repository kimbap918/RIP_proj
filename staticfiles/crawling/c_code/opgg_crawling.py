from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

path = "./chromedriver.exe"
driver = webdriver.Chrome(path, chrome_options=options)

driver.implicitly_wait(3)
url = "https://www.op.gg/champions?region=global"
# l = input()
# lanes = f'&tier=platinum_plus&position={l}'

driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

# # aside 캐릭터
# name = soup.select('#content-container > div.css-1fcwcq0.e2v0byd0 > aside > nav > ul > li > a > span')
# imgs = driver.find_elements(By.CSS_SELECTOR, '#content-container > div.css-1fcwcq0.e2v0byd0 > aside > nav > ul > li > a > img')
details = driver.find_elements(
    By.CSS_SELECTOR,
    "#content-container > div.css-1fcwcq0.e2v0byd0 > aside > nav > ul > li > a",
)
# # 챔피언 이름 담을 리스트
# c_name = []
# # 챔피언 이미지 담을 리스트
# c_img = []
# # 챔피언 디테일 주소 담을 리스트
c_detail = []

# # len(name) = 162
# for n in name:
#   c_name.append(n.text.strip())

# # # len(imgs) = 160
# for i in imgs:
#   c_img.append(i.get_attribute('src'))

# # # len(details) = 162
for d in details:
    c_detail.append(d.get_attribute("href"))

print(c_detail)
# # Json 영역
import json

# from collections import OrderedDict

# infos = []
# json 형태 저장하는걸 바꾸려면 여기수정
# for idx in range(len(c_name)):
#     infos.append({
#       'name' : c_name[idx],
#       'img' : c_img[idx],
#       'detail' : c_detail[idx]
#         })

# file_path = 'infos.json'
# # json 저장
# with open(file_path, 'w', encoding='utf-8') as f:
#     json.dump(infos, f, ensure_ascii=False, indent="\t")

# champs = []
# for i in range(len(c_detail)):
#     champs.append(
#         {
#             # 'name' : c_name[i],
#             # 'img' : c_img[i],
#             "detail": c_detail[i]
#         }
#     )
# print(champs)
# # main 탑
# # 탑 랭킹
# ranks = soup.select('#content-container > div.css-1fcwcq0.e2v0byd0 > main > div > table > tbody > tr > td.css-3bfwic.e1oulx2j4 > span:nth-child(1)')
# # 탑 챔피언 이미지
# r_imgs = driver.find_elements(By.CSS_SELECTOR, '#content-container > div.css-1fcwcq0.e2v0byd0 > main > div > table > tbody > tr > td.css-cym2o0.e1oulx2j6 > a > img')
# # 탐 챔피언 이름
# r_names = soup.select('#content-container > div.css-1fcwcq0.e2v0byd0 > main > div > table > tbody > tr > td.css-cym2o0.e1oulx2j6 > a > strong')
# # 탑 티어
# tiers = driver.find_elements(By.XPATH, '//*[@id="content-container"]/div[2]/main/div/table/tbody/tr/td[3]')
# # 탑 승률
# wins = soup.select('#content-container > div.css-1fcwcq0.e2v0byd0 > main > div > table > tbody > tr > td:nth-child(4)')
# # 탑 픽률
# picks = soup.select('#content-container > div.css-1fcwcq0.e2v0byd0 > main > div > table > tbody > tr > td:nth-child(5)')
# # 탑 밴률
# bens = soup.select('#content-container > div.css-1fcwcq0.e2v0byd0 > main > div > table > tbody > tr > td:nth-child(6)')
# # 탑 상대하기 어려운 챔피언
# hard_c = driver.find_elements(By.CSS_SELECTOR, '#content-container > div.css-1fcwcq0.e2v0byd0 > main > div > table > tbody > tr > td.css-8jdpx8.e1oulx2j2 > a > div > img')

# # 랭킹
# t_rank = []
# for r in ranks:
#   t_rank.append(r.text)

# # 이미지
# t_img = []
# for i in r_imgs:
#   t_img.append(i.get_attribute('src'))

# # 이름
# t_name = []
# for n in r_names:
#   t_name.append(n.text.strip())

# # 티어
# t_tier = []
# for r in tiers:
#   t_tier.append(r.text.strip())

# # 승률
# t_win = []
# for r in wins:
#   t_win.append(r.text.strip())

# # 픽률
# t_pick = []
# for r in picks:
#   t_pick.append(r.text.strip())

# # 티어
# t_ben = []
# for r in bens:
#   t_ben.append(r.text.strip())

# # 어려운 챔피언
# t_champ = []
# for c in hard_c:
#   t_champ.append(c.get_attribute('src'))

# # print(len(t_champ))

# t_3champ = []
# for i in range(60):
#   t_3champ.append(t_champ[i * 3 : (i * 3) + 3])

# # print(t_3champ)

# top = []
# for i in range(len(t_rank)):
#   top.append(
#     {
#       'rank' : t_rank[i],
#       'img' : t_img[i],
#       'name' : t_name[i],
#       'tier' : t_tier[i],
#       'win' : t_win[i],
#       'pick' : t_pick[i],
#       'ben' : t_ben[i],
#       'hard' : t_3champ[i]
#     }
#   )

# file_path = 'support.json'
# # json 저장
# with open(file_path, 'w', encoding='utf-8') as f:
#     json.dump(top, f, ensure_ascii=False, indent="\t")
