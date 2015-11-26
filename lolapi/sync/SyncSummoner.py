#!/usr/bin/env python
# -*- coding: utf-8 -*-

from local import *
import time
import datetime
from lolapi.core.SummonerHelper import *
from lolapi.core.NumberHelper import *
from lolapi.core.ApiHelper import *

class SyncSummoner:
    
    @staticmethod    
    def getSummoner(id, regiao):
        
        summoner    = Summoner(id, regiao)
        dados       = summoner.getSummonerDadosJSON()
        
        try:
            liga        = summoner.getLeague().get(str(id))[0]
        except:
            liga        = {}
        
        #status = summoner.getDisponibilidade()
        
        resultado = {}
        
        for k, v in  dados.items():
            
            timeUTC = str(v.get("revisionDate", ""))[:-3]
            
            revisaoDate = datetime.datetime.fromtimestamp( int(timeUTC) ).strftime('%Y-%m-%d %H:%M:%S')
            
            liga = SyncSummoner.getLeagueRankedSoloBySummoner(id, regiao)
            
            resultado = {
                "api_id" : id,
                "nivel"  : v.get("summonerLevel"),
                "nome"   : v.get("name"),
                "regiao" : regiao,
                "icone"  : v.get("profileIconId")
            }
            
            resultado.update(liga)
            
        return resultado
    
    @staticmethod 
    def getLeagueRankedSoloBySummoner(id, regiao):
        
        summoner    = Summoner(id, regiao)
        divisao = 0;
        tier = "Unranked"
        
        liga = None
        
        try:
            liga    = summoner.getLeague().get(str(id))[0]
        except:
            pass
        
        
        if not liga:
            resultado = { "tier" : "Unranked" }
        else:
            
            
            try:
                entry   = liga.get("entries",[])[0]
                divisao = Number.roman_to_int(str(entry.get("division")))
                tier    = liga.get("tier")
            except Exception as e:
                pass
                
            
            resultado = {
                "liga_nome" : liga.get("name"),
                "tier"      : tier,
                "divisao"   : divisao,
                "wins"  : entry.get("wins"),
                "loses"  : entry.get("losses"),
                "pdl"    : entry.get("leaguePoints"),
                "series" : entry.get("miniSeries", None)  
            }
            
        
        return resultado
        
    
    @staticmethod
    def getStatsRanked(id, regiao):
        
        summoner    = Summoner(id, regiao)
        
        try:
            resultado    = summoner.getStatsRanked()
        except Exception as e:
            raise Exception(str(e))
        
        campeoes = {}
        
        for r in resultado:
            stats = r.get("stats")
            campeao_id = r.get("id")
            
            campeoes[str(campeao_id)] = {
                "first_blood"       : stats.get("totalFirstBlood"),
                
                "torres_deburradas" : stats.get("totalTurretsKilled"),
                
                "partidas"          : stats.get("totalSessionsPlayed"),
                "vitorias"          : stats.get("totalSessionsWon"), 
                "derrotas"          : stats.get("totalSessionsLost"),
                
                "mortes_partida"    : stats.get("totalDeathsPerSession"),
                "maior_abate_partida"     : stats.get("mostChampionKillsPerSession"),
                
                "assistencias"          : stats.get("totalAssists"),
                "total_dano_feito"      : stats.get("totalDamageDealt"),
                "total_dano_recebido"   : stats.get("totalDamageTaken"),
                "total_dano_magico_feito" : stats.get("totalMagicDamageDealt"),
                
                "doublekill"        : stats.get("totalDoubleKills"),
                "triplekill"        : stats.get("totalTripleKills"),
                "quadrakill"        : stats.get("totalQuadraKills"),
                "pentakill"         : stats.get("totalPentaKills"),
                
                "gold"              : stats.get("totalGoldEarned"),
                "minions"           : stats.get("totalMinionKills"),
                
                "mortes"            : stats.get("maxNumDeaths"),
                "abates1"           : stats.get("maxChampionsKilled"),
                
                "abates"            : stats.get("totalChampionKills")
            }
            
        return campeoes
            
    @staticmethod 
    def getMatchesHistory(id, regiao):    
        
        matchHistory = []
        
        summoner    = Summoner(id, regiao)
        matches = {}
        
        try:
            matches    = summoner.getMatchHistory()
        except Exception as e:
            raise Exception(str(e))
        
        
        for match in matches.get("games", []):
            
            stats = match.get("stats",{})
            
            partida_args = {
                "partida_id": match.get("gameId"),
                "mapa_id"   : match.get("mapId"),
                "data_partida"  : match.get("createDate",0),
                "duracao"   : stats.get("timePlayed"),
                "modo" : match.get("gameMode"),
                "tipo" : match.get("subType"),
                "plataforma": match.get("gameType"),
                "regiao"    : regiao
            }
            
            
            invpartida_args = {
                 "invocador_id"  : id,
                 "campeao_id"    : match.get("championId"),
                 "ultimo_tier"   : None,
                 "participant_id": None,
                 "spell"         : match.get("spell1"),
                 "spell2"        : match.get("spell2"),
                 "time_id"       : match.get("teamId"),
                 "assists"       : stats.get("assists"),
                 "kills"         : stats.get("championsKilled"),
                 "deaths"        : stats.get("numDeaths"),
                 "level"        : stats.get("level"),
                 "combat_score" : None,
                 "double_kill"  : None,
                 "firstblood_assist" : None,
                 "firstblood_kill" : None,
                 "firsttower_assist" : None,
                 "firsttower_kill" : None,
                 "ouro_ganho" : stats.get("goldEarned"),
                 "ouro_gasto" : stats.get("goldSpent"),
                 "killing_spree" : stats.get("killingSprees"),
                 "maior_critico" : None,
                 "maior_ks" : stats.get("largestKillingSpree"),
                 "maior_multikill" : stats.get("largestMultikill"),
                 "danoap_recebido" : stats.get("magicDamageTaken"),
                 "danoap_recebido_champs" : stats.get("magicDamageDealtToChampions"),
                 "danoap_feito" : stats.get("magicDamageDealtPlayer"),
                 "minions_killed": stats.get("minionsKilled"),
                 "minions_neutro_killed" : stats.get("neutralMinionsKilled"),
                 "minions_neutro_killed_enemy" : None,
                 "pentakill" : None,
                 "danoad_recebido" : stats.get("physicalDamageTaken"),
                 "danoad_recebido_champs" : stats.get("physicalDamageDealtToChampions"),
                 "danoad_feito" : stats.get("physicalDamageDealtPlayer"),
                 "quadrakill" : None,
                 "wards" : None,
                 "total_dano_recebido" : stats.get("totalDamageTaken"),
                 "total_dano_recebido_champ": stats.get("totalDamageDealtToChampions"),
                 "total_dano_feito" : stats.get("totalDamageDealt"),
                 "total_cura" : stats.get("totalHeal"),
                 "total_tf" : None,
                 "total_unidades_curadas" :stats.get("totalUnitsHealed"),
                 "triplekill" : None,
                 "dano_verdadeiro_recebido" : stats.get("trueDamageTaken"),
                 "dano_verdadeiro_feito": stats.get("trueDamageDealtPlayer"),
                 "unrealkill" : None,
                 "pink_wards" : None,
                 "wards_killed" : stats.get("wardKilled"),
                 "wards_colocadas" :stats.get("wardPlaced"),
                 "winner" : stats.get("win")
            }
            
            matchHistory.append({
                "partida"               : partida_args,
                "invocadorpartida"      : invpartida_args
            })
            
        return matchHistory
            
    
   

         
        
    @staticmethod    
    def getSummonerByName(nome):
        
        
        nome = nome.replace(" ", "")
        _lista = []
        lista_busca = Summoner.getSummonersByName(nome)
        infos = {}
        
        for busca in lista_busca:
            
            try:
                infos = busca.get(nome,{})
            except:
                continue
            
            dict_summ = {
                "icone"  :  URL_ICONS_LOL.format(
                    icon_id = str(infos.get("profileIconId"))
                ),
                "id"     : infos.get("id"),
                "regiao" : busca.get("region"),
                "nome"   : infos.get("name"),
                "nivel"  : infos.get("summonerLevel"),
            }
            
            _lista.append(dict_summ)
            
        return _lista