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
        games = []
        players = []
        api_key = getattr(settings, "API_KEY", "API_KEY")
        summoner_url = (
            "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/"
            + summoner_name
            + "?api_key="
            + api_key
        )
        params = {"api_key": api_key}
        res = requests.get(summoner_url)

        if res.status_code == requests.codes.ok:  # 결과값이 정상적으로 반환되었을때만 실행하도록 설정
            summoner_exist = True
            summoners_result = res.json()  # response 값을 json 형태로 변환시키는 함수
            if summoners_result:
                sum_result["name"] = summoners_result["name"]
                print(summoners_result["puuid"])
                print(summoners_result["id"])
                sum_result["level"] = summoners_result["summonerLevel"]
                sum_result["profileIconId"] = summoners_result["profileIconId"]
                tier_url = (
                    "https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/"
                    + summoners_result["id"]
                )  # 소환사 티어 검색
                # print(tier_url)
                tier_info = requests.get(tier_url, params=params)
                tier_info = tier_info.json()
                print(tier_info)
                # print(tier_info)
                if len(tier_info) == 1:  # 자유랭크 또는 솔로랭크 둘중 하나만 있는경우
                    tier_info = tier_info.pop()
                    if tier_info["queueType"] == "RANKED_FLEX_SR":  # 자유랭크인 경우
                        team_tier["rank_type"] = "자유랭크 5:5"
                        team_tier["tier"] = tier_info["tier"]
                        team_tier["rank"] = tier_info["rank"]
                        team_tier["points"] = tier_info["leaguePoints"]
                        team_tier["wins"] = tier_info["wins"]
                        team_tier["losses"] = tier_info["losses"]
                    else:  # 솔로랭크인 경우
                        solo_tier["rank_type"] = "솔로랭크 5:5"
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

        # 최근 게임 10개 정보
        data = res.json()

        puu_id = data["puuid"]
        print(puu_id)
        matches_url = (
            "https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/"
            + puu_id
            + "/ids"
            + "?api_key="
            + api_key
        )

        mat = requests.get(matches_url)
        matches = mat.json()
        
        for match in matches[:10]:
            request_url = (
                "https://asia.api.riotgames.com/lol/match/v5/matches/"
                + match
                + "?api_key="
                + api_key
            )

            data = requests.get(request_url)
            data = data.json()

            p = data["info"]["gameDuration"]
            sec = int(p) % 60
            min = int(p) // 60
            play_time = f"{min}분 {sec}초"
            queue_id = data["info"]["queueId"]

            games.append({"play_time": play_time, "queue_id": queue_id, "min": min})
            # print(games)

            for part in data["info"]["participants"]:
                if  sum_result["name"] == part["summonerName"]:
                    player = dict()
                    player["participantId"] = part["participantId"]
                    player["championId"] = part["championId"]
                    player["championName"] = part["championName"]
                    player["summoner1Id"] = part["summoner1Id"]
                    player["summoner2Id"] = part["summoner2Id"]
                    player["summonerName"] = part["summonerName"]
                    player["summonerId"] = part["summonerId"]
                    player["kills"] = part["kills"]
                    player["deaths"] = part["deaths"]
                    player["assists"] = part["assists"]
                    player["goldEarned"] = part["goldEarned"]
                    player["goldEarnedPerMinute"] = round(part["goldEarned"] / min, 1)
                    player["totalDamageDealtToChampions"] = part["totalDamageDealtToChampions"]
                    player["magicDamageDealtToChampions"] = part["magicDamageDealtToChampions"]
                    player["physicalDamageDealtToChampions"] = part["physicalDamageDealtToChampions"]
                    player["trueDamageDealtToChampions"] = part["trueDamageDealtToChampions"]
                    player["totalDamageTaken"] = part["totalDamageTaken"]
                    player["totalHeal"] = part["totalHeal"]
                    player["doubleKills"] = part["doubleKills"]
                    player["tripleKills"] = part["tripleKills"]
                    player["quadraKills"] = part["quadraKills"]
                    player["pentaKills"] = part["pentaKills"]
                    player["item0"] = part["item0"]
                    player["item1"] = part["item1"]
                    player["item2"] = part["item2"]
                    player["item3"] = part["item3"]
                    player["item4"] = part["item4"]
                    player["item5"] = part["item5"]
                    player["item6"] = part["item6"]
                    player["win"] = part["win"]
                    player["visionScore"] = part["visionScore"]
                    player["totalMinionsKilled"] = part["totalMinionsKilled"]
                    player["totalMinionsKilledPerMinute"] = round(part["totalMinionsKilled"] / min, 1)
                    player["totalDamageDealtToChampions"] = part["totalDamageDealtToChampions"]
                    try:                            
                        player["stealthWardsPlaced"] = part["challenges"]["stealthWardsPlaced"]
                        player["kda"] = round(part["challenges"]["kda"], 2)
                    except KeyError:
                        print("해당 값 없음")
                    players.append(player) # 1챔프당 데이터
        #pp.pprint(players)
        # play_list.append(players) # 1게임당 모든 챔프 데이터
        game_list = zip(games, players)
        # pp.pprint(players)
        # print(games)
        return render(request, "summoners/result.html",
                {
                    "summoner_exist": summoner_exist,
                    "summoners_result": sum_result,
                    "solo_tier": solo_tier,
                    "team_tier": team_tier,
                    "play_time": play_time,
                    "queue_id": queue_id,
                    # "games": games,
                    # "players": players,
                    "game_list": game_list,
                },
            )