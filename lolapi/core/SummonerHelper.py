#!/usr/bin/env python
# -*- coding: utf-8 -*-


from local import *
from lolapi.core.ApiHelper import ApiHelper
import requests

class Summoner(object):
    
    def __init__(self, id, regiao):
        self.id = id        
        self.regiao = regiao
        
    def getSummonerDadosJSON(self): ##thrwo exception ApiException
        url = API_LOL_URL_SUMMONER
      
        url = url.format(
            summ_id = self.id
        )
        
        return ApiHelper.base_request(url, self.regiao)
        
    def getCurrentMatch(self):
       
       url = API_LOL_URL_CONSUMER_SPECTATOR
       url = url.format(
           region   = API_DICT_REGION_S.get(self.regiao),
           summ_id  = self.id 
       )
       
       return ApiHelper.observer_request(url, proxy=None)
       
    def getStatus(self):
       
        url = API_LOL_URL_CONSUMER_SPECTATOR
        url = url.format(
           region   = API_DICT_REGION_S.get(self.regiao),
           summ_id  = self.id 
        )
        
        match_current = ApiHelper.observer_request(url, proxy=None)
        return match_current.get("Success", False)


    def getLeague(self):
        
        url = API_LOL_URL_LEAGUE_BYSUMMONER_ENTRY
        url = url.format(
            summ_id = self.id
        )
        return ApiHelper.base_request(url, self.regiao)


    def getMatchHistory(self, champIds = None):
        
        url = "v1.3/game/by-summoner/{summ_id}/recent"
        url = url.format(
            summ_id = self.id
        )
 
        kwargs = { "beginIndex" : 0 , "endIndex"  : 1 , "championIds" : champIds }
        
        return ApiHelper.base_request(url, self.regiao, **kwargs)
        
    def getStatsRanked(self):
        
        url = "v1.3/stats/by-summoner/{summ_id}/ranked"
        url = url.format(
            summ_id = self.id
        )
        
        kwargs = {} #"SEASON" : 2015 }
        result = ApiHelper.base_request(url, self.regiao, **kwargs)
        return result.get("champions", [])
        
    @staticmethod    
    def getSummonersByName(nome):
     
        url = API_LOL_URL_SUMMONER_BYNAME
        url = url.format(
            nome = nome
        )
        
        lista_busca = []
        
        for region in API_LIST_REGION:
            try:
                result = ApiHelper.base_request(url, region)
                result["region"] = region
                lista_busca.append(result)
            except Exception as e:
               pass
        
        return lista_busca

