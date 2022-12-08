from django.shortcuts import render

# 라이엇 API 불러오기
from urllib import parse
import requests

# 라이엇 API 시크릿 키
from django.conf import settings

# 출력 확인용
import pprint

pp = pprint.PrettyPrinter(indent=4)


request_header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36",
    "Accept-Language": "ko,en-US;q=0.9,en;q=0.8,es;q=0.7",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": getattr(settings, "API_KEY", "API_KEY"),
}


# Create your views here.
def test(request):
    return render(request, "summoners/test.html")


def index(request):
    API_KEY = getattr(settings, "API_KEY", "API_KEY")

    return render(request, "summoners/index.html", {"api_key": API_KEY})


def result(request):
    if request.method == "GET":
        username = request.GET.get("search_text")
        summoner_name = parse.quote(username)

        summoner_exist = False
        sum_result = {}
        solo_tier = {}
        team_tier = {}
        store_list = []
        game_list = {}
        game_list2 = []
        api_key = getattr(settings, "API_KEY", "API_KEY")

        summoner_url = (
            "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/"
            + summoner_name
            + "?api_key="
            + api_key
        )  # 소환사 정보 검색
        params = {"api_key": api_key}
        # res = requests.get(summoner_url, params=params)
        res = requests.get(summoner_url)
        # print(res)
        # res = res.json()
        # summoners_result = json.loads(((res.text).encode('utf-8')))
        if res.status_code == requests.codes.ok:  # 결과값이 정상적으로 반환되었을때만 실행하도록 설정
            summoner_exist = True
            summoners_result = res.json()  # response 값을 json 형태로 변환시키는 함수
            if summoners_result:
                sum_result["name"] = summoners_result["name"]
                sum_result["level"] = summoners_result["summonerLevel"]
                sum_result["profileIconId"] = summoners_result["profileIconId"]
                # 최근 10게임 조회에 사용할 puuid
                sum_result["puuid"] = summoners_result["puuid"]
                tier_url = (
                    "https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/"
                    + summoners_result["id"]
                )  # 소환사 티어 검색
                # print(tier_url)
                tier_info = requests.get(tier_url, params=params)
                tier_info = tier_info.json()
                # print(tier_info)
                if len(tier_info) == 1:  # 자유랭크 또는 솔로랭크 둘중 하나만 있는경우
                    tier_info = tier_info.pop()
                    if tier_info["queueType"] == "RANKED_FLEX_SR":  # 자유랭크인 경우
                        team_tier["rank_type"] = "솔로랭크 5:5"
                        team_tier["tier"] = tier_info["tier"]
                        team_tier["rank"] = tier_info["rank"]
                        team_tier["points"] = tier_info["leaguePoints"]
                        team_tier["wins"] = tier_info["wins"]
                        team_tier["losses"] = tier_info["losses"]
                    else:  # 솔로랭크인 경우
                        solo_tier["rank_type"] = "자유랭크 5:5"
                        solo_tier["tier"] = tier_info["tier"]
                        solo_tier["rank"] = tier_info["rank"]
                        solo_tier["points"] = tier_info["leaguePoints"]
                        solo_tier["wins"] = tier_info["wins"]
                        solo_tier["losses"] = tier_info["losses"]
                if len(tier_info) == 2:  # 자유랭크, 솔로랭크 둘다 전적이 있는경우
                    for item in tier_info:
                        store_list.append(item)
                    solo_tier["rank_type"] = "자유랭크 5:5"
                    solo_tier["tier"] = store_list[0]["tier"]
                    solo_tier["rank"] = store_list[0]["rank"]
                    solo_tier["points"] = store_list[0]["leaguePoints"]
                    solo_tier["wins"] = store_list[0]["wins"]
                    solo_tier["losses"] = store_list[0]["losses"]

                    team_tier["rank_type"] = "솔로랭크 5:5"
                    team_tier["tier"] = store_list[1]["tier"]
                    team_tier["rank"] = store_list[1]["rank"]
                    team_tier["points"] = store_list[1]["leaguePoints"]
                    team_tier["wins"] = store_list[1]["wins"]
                    team_tier["losses"] = store_list[1]["losses"]

        return render(
            request,
            "summoners/result.html",
            {
                "summoner_exist": summoner_exist,
                "summoners_result": sum_result,
                "solo_tier": solo_tier,
                "team_tier": team_tier,
            },
        )


# 1. https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/ 에서 puuid 값을 가져온다.

# 2. 가져온 puuid값을https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start={start}&count={count} 에 넘겨준다.

#    여기서 puuid : 소환사 고유 puuid, start : 가장 최근 경기부터 알고 싶으면 0, (예 : 가장 최근에 했던 3번째 경기부터 알고 싶다면 3), count : 결과를 몇개 까지 받을지 (max : 100)

# 3. 2에서 받은 결과 값은 KR_6244514829의 형태로(matchId) 저장되는데, https://asia.api.riotgames.com/lol/match/v5/matches/{matchId} 를 통해 게임 상세정보를 알수있다.


# puuid : 소환사 고유 puuid
# start : 가장 최근 경기부터 알고 싶으면 0, (예 : 가장 최근에 했던 3번째 경기부터 알고 싶다면 3)
# count : 결과를 몇개 까지 받을지 (max : 100)
def match_v5_get_list_match_id(puuid, start, count):
    url = f"https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start={start}&count={count}"
    return requests.get(url, headers=request_header).json()


# queueId : 솔랭 - 420, 노말 - 430, 팀랭 - 440
# gameDuration : 게임 길이
# championId : 챔프명
# summoner1Id : D키에 해당하는 서머너스펠
# summoner2Id : F키에 해당하는 서머너스펠
# summonerName : 소환사 닉네임
# puuid : 소환사 고유 이름
# kills : K
# deaths : D
# assists : A
# kda : KDA((kill + assist) / death,)
# totalMinionsKilled : cs
# item0 ~ 6 : 장비한 아이템 코드(총 7개)
# totalDamageDealtToChampions : 챔피언에게 가한 피해
# win : 승패여부
# visionScore : 시야점수
# stealthWardsPlaced : 제어와드 설치 개수
def match_v5_get_match_history(matchId):
    url = f"https://asia.api.riotgames.com/lol/match/v5/matches/{matchId}"

    return requests.get(url, headers=request_header).json()


# pp.pprint(match_v5_get_match_history('KR_6244514829'))
