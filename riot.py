import requests
from urllib import parse
import time
 
api_key = "RGAPI-8c39dcd3-5856-4ef6-a66d-ee288226d2a8"
request_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": "RGAPI-8c39dcd3-5856-4ef6-a66d-ee288226d2a8"
}
 
# def check_my_team(*args):
#     current_players = []
#     for n in range(0, 4):
#         name = args[n]
#         print(name)
#         encoded_name = parse.quote(name)
#         current_players.append(encoded_name)
#         summoner_account_id = requests.get("https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + encoded_name, headers=request_headers).json()["accountId"]
#         win = 0
#         for n in range(0, 10):
#             get_latest_match_id = requests.get("https://kr.api.riotgames.com/lol/match/v4/matchlists/by-account/" + summoner_account_id, headers=request_headers).json()["matches"][n]["gameId"]
#             get_match_info = requests.get("https://kr.api.riotgames.com/lol/match/v4/matches/" + str(get_latest_match_id), headers=request_headers).json()
#             for i in range(0, 10):
#                 if get_match_info["participantIdentities"][i]["player"]["summonerName"] == name:
#                     if get_match_info["participants"][i]["stats"]["win"] == True:
#                         win += 1
#             time.sleep(1)
#         print(win)
#         time.sleep(2)
            
#         latest_players = []
#         for n in range(0, 10):
#             get_latest_match_id = requests.get("https://kr.api.riotgames.com/lol/match/v4/matchlists/by-account/" + summoner_account_id, headers=request_headers).json()["matches"][0]["gameId"]
#             get_match_info = requests.get("https://kr.api.riotgames.com/lol/match/v4/matches/" + str(get_latest_match_id), headers=request_headers).json()
#             latest_players.append(get_match_info["participantIdentities"][n]["player"]["summonerName"])
#             time.sleep(1)
#         print(latest_players)
#         if len(set(current_players) & set(latest_players)) > 1:
#             print(set(current_players) & set(latest_players))
#         else:
#             print("듀오가 없습니다")
#         time.sleep(2)
 
# check_my_team("내 팀원1","내 팀원2","내 팀원3", "내 팀원4")
 
# def check_members():
#     print("시작")
#     live_game = requests.get("https://kr.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/E1AfcxGWK9MaVl7tn6uMcdFNLEFKh3gx3cAEhrm4Wq0iDQ", headers=request_headers)
#     live_game = live_game.json()
#     current_players = []
#     print("진행중")
#     print(live_game)
#     for n in range(0, 10):
#         print("??")
#         name = parse.quote(live_game["participants"][n]["summonerName"])
#         print(name)
#         current_players.append(name)
#         summoner_account_id = requests.get("https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + name, headers=request_headers).json()["accountId"]
#         get_latest_match_id = requests.get("https://kr.api.riotgames.com/lol/match/v4/matchlists/by-account/" + summoner_account_id, headers=request_headers).json()["matches"][0]["gameId"]
#         get_match_info = requests.get("https://kr.api.riotgames.com/lol/match/v4/matches/" + str(get_latest_match_id), headers=request_headers).json()
#         latest_players = []
#         for n in range(0, 10):
#             latest_players.append(get_match_info["participantIdentities"][n]["player"]["summonerName"])
#             if len(set(current_players) & set(latest_players)) > 1:
#                 print(set(current_players) & set(latest_players))
#         time.sleep(2)
 
# check_members()

# name = request.GET['summoner_name']
name = '안녕'
summoner_name = parse.quote(name)
# url에 담게 인코딩

request_url = 'https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + summoner_name + '?api_key=' + api_key
time.sleep(2)
data = requests.get(request_url)
data = data.json()
# dict으로 변환

# account_id = data['accountId']
account_id = 'hello'
# accountId를 가져왔다.

time.sleep(2)
# request_url = 'https://kr.api.riotgames.com/lol/match/v4/matchlists/by-account/' + summoner['account_id'] + '?api_key=' + api_key
request_url = 'https://kr.api.riotgames.com/lol/match/v4/matchlists/by-account/' + 'hello' + '?api_key=' + api_key

data = requests.get(request_url)
matches = data.json()['matches']
# matchlist를 쭉 가져온다.


for match in matches:

    request_url = 'https://kr.api.riotgames.com/lol/match/v4/matches/' + str(match['gameId']) + '?api_key=' + api_key
    # gameId는 int니까 형변환
    data = requests.get(request_url)
    data = data.json()

    play_time = data['gameDuration']
    queue_id = data['queueId']
    time.sleep(2)
    players = []
    # 각 플레이어들의 정보를 담아보자.
    for part in data['participants']:
        player = dict()
        player['id'] = part['participantId']
        player['champion'] = part['championId']
        player['spell1'] = part['spell1Id']
        player['spell2'] = part['spell2Id']
        player['level'] = part['stats']['champLevel']
        player['kills'] = part['stats']['kills']
        player['deaths'] = part['stats']['deaths']
        player['assists'] = part['stats']['assists']
        player['kda'] = round((player['kills'] + player['assists']) / player['deaths'], 2)
        player['item0'] = part['stats']['item0']
        player['item1'] = part['stats']['item1']
        player['item2'] = part['stats']['item2']
        player['item3'] = part['stats']['item3']
        player['item4'] = part['stats']['item4']
        player['item5'] = part['stats']['item5']
        player['item6'] = part['stats']['item6']
        player['visionscore'] = part['stats']['visionScore']
        player['gold'] = part['stats']['goldEarned']
        player['cs'] = part['stats']['totalMinionsKilled']
        players.append(player)

print(players)