from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

path = "./chromedriver.exe" 
driver = webdriver.Chrome(path, chrome_options=options)

driver.implicitly_wait(3)

driver.get('https://www.op.gg/champions?region=tr') 
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser') 
name = soup.select('#content-container > div.css-1fcwcq0.e2v0byd0 > aside > nav > ul > li > a > span')
imgs = driver.find_elements(By.CSS_SELECTOR, '#content-container > div.css-1fcwcq0.e2v0byd0 > aside > nav > ul > li > a > img')
details = driver.find_elements(By.CSS_SELECTOR, '#content-container > div.css-1fcwcq0.e2v0byd0 > aside > nav > ul > li > a')
# 챔피언 이름 담을 리스트
c_name = []
# 챔피언 이미지 담을 리스트
c_img = []
# 챔피언 디테일 주소 담을 리스트
c_detail = []

# len(name) = 162
for n in name:
  c_name.append(n.text.strip())

c_name.remove('아이번')
c_name.remove('스카너')

# len(imgs) = 160
for i in imgs:
  c_img.append(i.get_attribute('src'))

# len(details) = 162
for d in details:
  c_detail.append(d.get_attribute('href'))

c_detail.remove('https://www.op.gg/champions/ivern?region=tr&tier=platinum_plus')
c_detail.remove('https://www.op.gg/champions/skarner?region=tr&tier=platinum_plus')
# print(c_detail)
# print(len(c_detail))

champs = []
for i in range(len(c_name)):
  champs.append(
    {
      'name' : c_name[i],
      'img' : c_img[i],
      'detail' : c_detail[i]
    }
  )

for c in champs:
  print(c['name'])
  print(c['img'])
  print(c['detail'])