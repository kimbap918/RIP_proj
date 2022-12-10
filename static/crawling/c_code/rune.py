link = [
    "https://www.op.gg/champions/khazix/jungle/build?region=global&tier=platinum_plus"
    # "https://www.op.gg/champions/zoe/mid?region=global&tier=platinum_plus",
    # "https://www.op.gg/champions/ziggs/mid?region=global&tier=platinum_plus",
    # "https://www.op.gg/champions/jhin/adc?region=global&tier=platinum_plus",
    # "https://www.op.gg/champions/zilean/support?region=global&tier=platinum_plus",
    # "https://www.op.gg/champions/jinx/adc?region=global&tier=platinum_plus",
    # "https://www.op.gg/champions/chogath/top?region=global&tier=platinum_plus",
    # "https://www.op.gg/champions/karma/support?region=global&tier=platinum_plus",
    # "https://www.op.gg/champions/camille/top?region=global&tier=platinum_plus",
    # "https://www.op.gg/champions/kassadin/mid?region=global&tier=platinum_plus",
    # "https://www.op.gg/champions/karthus/jungle?region=global&tier=platinum_plus",
    # "https://www.op.gg/champions/cassiopeia/mid?region=global&tier=platinum_plus",
    # "https://www.op.gg/champions/kaisa/adc?region=global&tier=platinum_plus",
    # "https://www.op.gg/champions/khazix/jungle?region=global&tier=platinum_plus",
    # "https://www.op.gg/champions/katarina/mid?region=global&tier=platinum_plus",
    # "https://www.op.gg/champions/kalista/adc?region=global&tier=platinum_plus",
    # "https://www.op.gg/champions/kennen/top?region=global&tier=platinum_plus",
    # "https://www.op.gg/champions/caitlyn/adc?region=global&tier=platinum_plus",
    # "https://www.op.gg/champions/kayn/jungle?region=global&tier=platinum_plus",
    # "https://www.op.gg/champions/kayle/top?region=global&tier=platinum_plus",
    # "https://www.op.gg/champions/kogmaw/adc?region=global&tier=platinum_plus",
    # "https://www.op.gg/champions/corki/mid?region=global&tier=platinum_plus",
    # "https://www.op.gg/champions/quinn/top?region=global&tier=platinum_plus",
    # "https://www.op.gg/champions/ksante/top?region=global&tier=platinum_plus",
    # "https://www.op.gg/champions/kled/top?region=global&tier=platinum_plus",
    # "https://www.op.gg/champions/qiyana/mid?region=global&tier=platinum_plus",
    # "https://www.op.gg/champions/kindred/jungle?region=global&tier=platinum_plus",
    # "https://www.op.gg/champions/taric/support?region=global&tier=platinum_plus",
    # "https://www.op.gg/champions/talon/mid?region=global&tier=platinum_plus",
    # "https://www.op.gg/champions/taliyah/jungle?region=global&tier=platinum_plus",
    # "https://www.op.gg/champions/tahmkench/top?region=global&tier=platinum_plus",
    # "https://www.op.gg/champions/trundle/jungle?region=global&tier=platinum_plus",
    # "https://www.op.gg/champions/tristana/adc?region=global&tier=platinum_plus",
    # "https://www.op.gg/champions/tryndamere/top?region=global&tier=platinum_plus",
    # "https://www.op.gg/champions/twistedfate/mid?region=global&tier=platinum_plus",
    # "https://www.op.gg/champions/twitch/adc?region=global&tier=platinum_plus",
    # "https://www.op.gg/champions/teemo/top?region=global&tier=platinum_plus",
    # "https://www.op.gg/champions/pyke/support?region=global&tier=platinum_plus",
    # "https://www.op.gg/champions/pantheon/support?region=global&tier=platinum_plus",
    # "https://www.op.gg/champions/fiddlesticks/jungle?region=global&tier=platinum_plus",
    # "https://www.op.gg/champions/fiora/top?region=global&tier=platinum_plus",
    # "https://www.op.gg/champions/fizz/mid?region=global&tier=platinum_plus",
    # "https://www.op.gg/champions/heimerdinger/support?region=global&tier=platinum_plus",
    # "https://www.op.gg/champions/hecarim/jungle?region=global&tier=platinum_plus",
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

    r1_1 = driver.find_elements(
        By.CSS_SELECTOR,
        "#content-container > main > div:nth-child(1) > div > div > div > div > div:nth-child(1) > div:nth-child(3) > div > div > div > img",
    )

    r1_2 = driver.find_elements(
        By.CSS_SELECTOR,
        "#content-container > main > div:nth-child(1) > div > div > div > div > div:nth-child(1) > div:nth-child(4) > div > div > div > img",
    )

    r1_3 = driver.find_elements(
        By.CSS_SELECTOR,
        "#content-container > main > div:nth-child(1) > div > div > div > div > div:nth-child(1) > div:nth-child(5) > div > div > div > img",
    )

    r1_4 = driver.find_elements(
        By.CSS_SELECTOR,
        "#content-container > main > div:nth-child(1) > div > div > div > div > div:nth-child(1) > div:nth-child(6) > div > div > div > img",
    )

    r2_1 = driver.find_elements(
        By.CSS_SELECTOR,
        "#content-container > main > div:nth-child(1) > div > div > div > div > div:nth-child(3) > div:nth-child(3) > div > div > div > img",
    )

    r2_2 = driver.find_elements(
        By.CSS_SELECTOR,
        "#content-container > main > div:nth-child(1) > div > div > div > div > div:nth-child(3) > div:nth-child(4) > div > div > div > img",
    )

    r2_3 = driver.find_elements(
        By.CSS_SELECTOR,
        "#content-container > main > div:nth-child(1) > div > div > div > div > div:nth-child(3) > div:nth-child(5) > div > div > div > img",
    )

    # 챔피언 이름 담을 리스트
    c_name = []
    c_r1_1 = []
    c_r1_2 = []
    c_r1_3 = []
    c_r1_4 = []

    c_r2_1 = []
    c_r2_2 = []
    c_r2_3 = []

    # len(name) = 162
    for n in name:
        c_name.append(n.text.strip())

    for i in r1_1:
        c_r1_1.append(i.get_attribute("src"))

    for i in r1_2:
        c_r1_2.append(i.get_attribute("src"))

    for i in r1_3:
        c_r1_3.append(i.get_attribute("src"))

    for i in r1_4:
        c_r1_4.append(i.get_attribute("src"))

    for i in r2_1:
        c_r2_1.append(i.get_attribute("src"))

    for i in r2_2:
        c_r2_2.append(i.get_attribute("src"))

    for i in r2_3:
        c_r2_3.append(i.get_attribute("src"))

    champ = {}
    champ["name"] = c_name
    champ["r1_1"] = c_r1_1
    champ["r1_2"] = c_r1_2
    champ["r1_3"] = c_r1_3
    champ["r1_4"] = c_r1_4
    champ["r2_1"] = c_r2_1
    champ["r2_2"] = c_r2_2
    champ["r2_3"] = c_r2_3

    champ_detail.append(champ)

# print(champ_detail)


import json

file_path = "champ_rune.json"
# json 저장
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(champ_detail, f, ensure_ascii=False, indent="\t")
