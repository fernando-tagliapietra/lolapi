# -*- coding: utf-8 -*- 

API_KEY = [ "123" ]


MSG_ERROR_NOT_AUTH = "Key inválida"

REGEX_EMAIL = r"^[^@]+@[^@]+\.[^@]+$"
#REGEX_EMAIL = r"^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$"




###ALTER TABLE Usuario ADD nome varchar(50) AFTER id

RIOT_API_KEY =  "b08fa73d-b4a3-41a8-9e3e-1d7b7df509be"
URL_API_OBSERVER_SPECTATE = " https://na.api.pvp.net/observer-mode/rest/consumer/getSpectatorGameInfo/%s/%s/?api_key=b08fa73d-b4a3-41a8-9e3e-1d7b7df509be"

API_DICT_REGION_S = { 
    "BR"   : "BR1", 
    "EUNE" : "EUNE1", 
    "EUW"  : "EUW1", 
    "KR"   : "KR", 
    "LAN"  : "LAN1", 
    "LAS"  : "LAS1", 
    "NA"   : "NA1", 
    "OCE"  : "OCE1", 
    "RU"   : "RU", 
    "TR" : "TR1" 
}


URL_API_LOL = "https://br.api.pvp.net/api/lol/{region}/v1.4"
URL_TIER_LOL ="http://loldb.gameguyz.com/images/champion_rank/{tier}_{divisao}.png"

API_LIST_REGION = ["BR", "EUNE", "EUW", "KR", "LAN", "LAS", "NA", "OCE", "RU", "TR"]

URL_ICONS_LOL=  "http://lkimg.zamimg.com/shared/riot/images/profile_icons/profileIcon{icon_id}.jpg"
#"http://ddragon.leagueoflegends.com/cdn/5.2.1/img/profileicon/"
URL_LOL = "https://porject-loldemo-fernando-tagliapietra.c9.io/"
APP_LOL_SUMMONER = "summoner"
APP_LOL_SUMMONERDETAIL = "summonerdetail"
    
    
API_LOL_PROXY_DEFAULT = "na"

API_LOL_URL_CHAMPION = "v1.2/champion"
API_LOL_URL_ITEM = "v1.2/item"

API_LOL_URL_SUMMONER = "v1.4/summoner/{summ_id}"
API_LOL_URL_SUMMONER_BYNAME = "v1.4/summoner/by-name/{nome}"
API_LOL_URL_CONSUMER_SPECTATOR = "consumer/getSpectatorGameInfo/{region}/{summ_id}/"
API_LOL_URL_LEAGUE_BYSUMMONER_ENTRY = "v2.5/league/by-summoner/{summ_id}/entry"


REGEX_EMAIL = r"[^@]+@[^@]+\.[^@]+"


URL_API = "https://lolapi-fernando-tagliapietra.c9.io"
URL_API_VERSAO = "/api/v1"


