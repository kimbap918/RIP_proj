from django.shortcuts import render
# OP.GG 웹크롤링 라이브러리
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# 크롤링
path = "./chromedriver.exe" 
driver = webdriver.Chrome(path, chrome_options=options)
# 3초 타이머
driver.implicitly_wait(3)
# OP.GG 챔피언 정보 페이지 주소
driver.get('https://www.op.gg/champions?region=tr') 
# 페이지의 요소
html = driver.page_source
# 페이지 요소 요청하기
soup = BeautifulSoup(html, 'html.parser')
# 챔피언 이름
name = soup.select('#content-container > div.css-1fcwcq0.e2v0byd0 > aside > nav > ul > li > a > span')
# 챔피언 이미지
imgs = driver.find_elements(By.CSS_SELECTOR, '#content-container > div.css-1fcwcq0.e2v0byd0 > aside > nav > ul > li > a > img')
# 챔피언 디테일 페이지 주소
details = driver.find_elements(By.CSS_SELECTOR, '#content-container > div.css-1fcwcq0.e2v0byd0 > aside > nav > ul > li > a')


# 챔피언 이름 담을 리스트
c_name = []
# 챔피언 이미지 담을 리스트
c_img = []
# 챔피언 디테일 주소 담을 리스트
c_detail = []

# 크롤링한 챔피언 이름 리스트에 저장
for n in name:
    c_name.append(n.text.strip())

# 이미지 없는 챔피언 이름 리스트에서 삭제
c_name.remove('아이번')
c_name.remove('스카너')

# 크롤링한 이미지 주소 리스트에 저장
for i in imgs:
    c_img.append(i.get_attribute('src'))

# 크롤링한 디테일 주소 리스트에 저장
for d in details:
  c_detail.append(d.get_attribute('href'))

# 이미지 없는 챔피언 주소 리스트에서 삭제
c_detail.remove('https://www.op.gg/champions/ivern?region=tr&tier=platinum_plus')
c_detail.remove('https://www.op.gg/champions/skarner?region=tr&tier=platinum_plus')

# 챔피언 정보 딕셔너리로 저장
champs = []
for i in range(len(c_name)):
  champs.append(
    {
      'name' : c_name[i],
      'img' : c_img[i],
      'detail' : c_detail[i]
    }
  )

# main 탑
# 탑 랭킹
ranks = soup.select('#content-container > div.css-1fcwcq0.e2v0byd0 > main > div > table > tbody > tr > td.css-3bfwic.e1oulx2j4 > span:nth-child(1)')
# 탑 챔피언 이미지
r_imgs = driver.find_elements(By.CSS_SELECTOR, '#content-container > div.css-1fcwcq0.e2v0byd0 > main > div > table > tbody > tr > td.css-cym2o0.e1oulx2j6 > a > img')
# 탐 챔피언 이름
r_names = soup.select('#content-container > div.css-1fcwcq0.e2v0byd0 > main > div > table > tbody > tr > td.css-cym2o0.e1oulx2j6 > a > strong')
# 탑 티어 
tiers = driver.find_elements(By.XPATH, '//*[@id="content-container"]/div[2]/main/div/table/tbody/tr/td[3]')
# 탑 승률
wins = soup.select('#content-container > div.css-1fcwcq0.e2v0byd0 > main > div > table > tbody > tr > td:nth-child(4)')
# 탑 픽률
picks = soup.select('#content-container > div.css-1fcwcq0.e2v0byd0 > main > div > table > tbody > tr > td:nth-child(5)')
# 탑 밴률
bens = soup.select('#content-container > div.css-1fcwcq0.e2v0byd0 > main > div > table > tbody > tr > td:nth-child(6)')
# 탑 상대하기 어려운 챔피언
# hard_c = driver.find_elements(By.CSS_SELECTOR, '#content-container > div.css-1fcwcq0.e2v0byd0 > main > div > table > tbody > tr > td.css-8jdpx8.e1oulx2j2')

# 랭킹
t_rank = []
for r in ranks:
  t_rank.append(r.text)

# 이미지
t_img = []
for i in r_imgs:
  t_img.append(i.get_attribute('src'))
  
# 이름
t_name = []
for n in r_names:
  t_name.append(n.text.strip())

# 티어
t_tier = []
for r in tiers:
  t_tier.append(r.text.strip())

# 승률
t_win = []
for r in wins:
  t_win.append(r.text.strip())

# 픽률
t_pick = []
for r in picks:
  t_pick.append(r.text.strip())

# 티어
t_ben = []
for r in bens:
  t_ben.append(r.text.strip())

# 어려운 챔피언
# t_champ = []
# for c in hard_c:
#   t_champ.append(c.get_attribute('alt'))


ranking = []
for i in range(len(t_rank)):
  ranking.append(
    {
      'rank' : t_rank[i],
      'img' : t_img[i],
      'name' : t_name[i],
      'tier' : t_tier[i],
      'win' : t_win[i],
      'pick' : t_pick[i],
      'ben' : t_ben[i],
      # 'hard' : t_champ[i]
    }
  )

# Create your views here.
def index(request):

    # for champ in champs:
    #     name = champ['name']
    #     img = champ['img']

    context = {
        # 'name' : name,
        # 'img' : img,
        'champs' : champs,
        'ranking' : ranking,
    }
    return render(request, 'champions/index.html', context)

def detail(request, c_name):
    for champ in champs:
        detail = champ['detail']
    
    context = {
        'detail' : detail,
    }
    return render(request, 'champions/detail.html', context)