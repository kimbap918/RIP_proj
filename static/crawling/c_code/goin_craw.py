link = [
    "https://www.op.gg/champions/gragas/top?region=global&tier=platinum_plus",
    "https://www.op.gg/champions/malphite/top?region=global&tier=platinum_plus",
    "https://www.op.gg/champions/kayle/top?region=global&tier=platinum_plus",
    "https://www.op.gg/champions/volibear/top?region=global&tier=platinum_plus",
    "https://www.op.gg/champions/tahmkench/top?region=global&tier=platinum_plus",
    "https://www.op.gg/champions/ivern/jungle?region=global&tier=platinum_plus",
    "https://www.op.gg/champions/skarner/jungle?region=global&tier=platinum_plus",
    "https://www.op.gg/champions/nidalee/jungle?region=global&tier=platinum_plus",
    "https://www.op.gg/champions/jarvaniv/jungle?region=global&tier=platinum_plus",
    "https://www.op.gg/champions/shaco/jungle?region=global&tier=platinum_plus",
    "https://www.op.gg/champions/aurelionsol/mid?region=global&tier=platinum_plus",
    "https://www.op.gg/champions/ryze/mid?region=global&tier=platinum_plus",
    "https://www.op.gg/champions/azir/mid?region=global&tier=platinum_plus",
    "https://www.op.gg/champions/corki/mid?region=global&tier=platinum_plus",
    "https://www.op.gg/champions/annie/mid?region=global&tier=platinum_plus",
    "https://www.op.gg/champions/zeri/adc?region=global&tier=platinum_plus",
    "https://www.op.gg/champions/kalista/adc?region=global&tier=platinum_plus",
    "https://www.op.gg/champions/aphelios/adc?region=global&tier=platinum_plus",
    "https://www.op.gg/champions/sivir/adc?region=global&tier=platinum_plus",
    "https://www.op.gg/champions/vayne/adc?region=global&tier=platinum_plus",
    "https://www.op.gg/champions/pantheon/support?region=global&tier=platinum_plus",
    "https://www.op.gg/champions/zyra/support?region=global&tier=platinum_plus",
    "https://www.op.gg/champions/brand/support?region=global&tier=platinum_plus",
    "https://www.op.gg/champions/xerath/support?region=global&tier=platinum_plus",
    "https://www.op.gg/champions/janna/support?region=global&tier=platinum_plus",
]


from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

path = "./chromedriver.exe"
driver = webdriver.Chrome(path, chrome_options=options)

champ_detail = []

for url in link:
    driver.implicitly_wait(3)
    # url = i

    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    name = driver.find_elements(
        By.CSS_SELECTOR,
        "#content-header > div.css-cwly3v.e8u7qho8 > div.inner > div:nth-child(1) > div.css-1a9mfwh.e1mrkevn4 > div.info-box > h1 > span.name",
    )

    jangin = driver.find_elements(
        By.CSS_SELECTOR,
        "#content-container > aside > div:nth-child(3) > h3 > a",
    )

    rank = driver.find_elements(
        By.CSS_SELECTOR,
        "#content-container > aside > div:nth-child(3) > div > div > ul > li > div.rank-summoner > div.rank",
    )

    imgs = driver.find_elements(
        By.CSS_SELECTOR,
        "#content-container > aside > div:nth-child(3) > div > div > ul > li > div.rank-summoner > div.summoner > a > img",
    )

    jname = driver.find_elements(
        By.CSS_SELECTOR,
        "#content-container > aside > div:nth-child(3) > div > div > ul > li > div.rank-summoner > div.summoner > a",
    )

    count = driver.find_elements(
        By.CSS_SELECTOR,
        "#content-container > aside > div:nth-child(3) > div > div > ul > li > div.game-count > strong",
    )

    # 챔피언 이름 담을 리스트
    c_name = []
    # 챔피언 이미지 담을 리스트
    c_jangin = []
    c_rank = []
    c_imgs = []
    c_jname = []
    c_count = []

    # len(name) = 162
    for n in name:
        c_name.append(n.text.strip())

    for n in jangin:
        c_jangin.append(n.text.strip())

    for n in rank:
        c_rank.append(n.text.strip())

    for i in imgs:
        c_imgs.append(i.get_attribute("src"))

    for n in jname:
        c_jname.append(n.text.strip())

    for n in count:
        c_count.append(n.text.strip())

    champ = {}
    champ["name"] = c_name[0]
    champ["lane"] = c_jangin[0]
    # 3
    champ["rank"] = c_rank
    champ["imgs"] = c_imgs
    champ["jname"] = c_jname
    champ["count"] = c_count

    champ_detail.append(champ)

# print(champ_detail)


import json

file_path = "champ_jangin.json"
# json 저장
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(champ_detail, f, ensure_ascii=False, indent="\t")
