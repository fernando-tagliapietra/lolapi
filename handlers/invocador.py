# -*- coding: utf-8 -*- 
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from lolapi.models import Invocador, Partida, InvocadorPartida
from lolapi._serializers.InvocadorSerializer import InvocadorSerializer
from lolapi._serializers.InvocadorPartidaSerializer import InvocadorPartidaSerializer
from lolapi._serializers.PartidaSerializer import PartidaSerializer

from rest_framework import status

from lolapi.core.SummonerHelper import *
from lolapi.sync.SyncSummoner import *

import datetime
        
@api_view(['GET'])
def listar(request):
    
    busca = request.GET.get("busca")
    kwargs = {}
        
    if busca:
        kwargs["nome__in"] = busca
            
    invocadores = Invocador.objects.filter(**kwargs)
    serializer = InvocadorSerializer(invocadores, many=True)
    result = {"Success" : True, "invocadores": serializer.data }
    return Response (result)


@api_view(['POST'])
def adicionar(request):
    
        apid        = request.POST.get("apid")
        nome        = request.POST.get("nome")
        tier        = request.POST.get("tier")
        divisao     = request.POST.get("divisao")
        icone       = request.POST.get("icone")
        nivel       = request.POST.get("nivel")
        regiao      = request.POST.get("regiao")
        liga_nome   = request.POST.get("liga_nome")
        liga_id     = request.POST.get("liga_id")
        pdl         = request.POST.get("pdl")
        wins        = request.POST.get("wins")
        loses       = request.POST.get("loses")
        series      = request.POST.get("series")
        
        if not apid or not nome:
            return Response({"Success": False, "msg": "Parametros obrigatorios inválidos"})
        
        data = {
            'api_id': apid,
            'nome': nome,
            'tier': tier,
            'divisao' : divisao,
            'icone': icone,
            'nivel': nivel,
            'regiao': regiao,
            'liga_nome': liga_nome,
            'liga_id': liga_id,
            'pdl': pdl,
            'wins': wins,
            'loses': loses,
            'series': series
        }
            
        serializer = InvocadorSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"Success": True})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


@api_view(['POST'])
def selecionar(request, sync=None):
    
    apid        = request.POST.get("apid")
    regiao      = request.POST.get("regiao")
    matchs = []
   
    if not apid or not regiao:
        return Response({"Success": False, "msg": "Parametros obrigatorios inválidos"})
    
    
    #championStats = SyncSummoner.getStatsRanked(apid, regiao)
    #return Response({"Success" : True, "lafora" : championStats})
    
    invocadores = Invocador.objects.filter(api_id=apid)
    
    try:
        
        if invocadores and not sync:
            invocador = invocadores[0]   
        else:
            dados_invocador = SyncSummoner.getSummoner(apid, regiao)
            #championStats   = SyncSummoner.getStatsRanked(apid, regiao) #statsranked
            #TODO Alterar StatsRanked
            
            if invocadores:
                invocador = invocadores[0]
                dados_invocador["id"] = invocador.id
                dados_invocador["data_atualizacao"] = datetime.datetime.now()
                
            invocador = Invocador(**dados_invocador)
            invocador.save()
         
            
            
        if sync:
            
            _matchs = SyncSummoner.getMatchesHistory(apid, regiao)
            
            for match in _matchs:
                
                partida = match.get("partida",{})
                
                partidas = Partida.objects.filter(partida_id = partida.get("partida_id"))
                
                if partidas:
                    new_partida = partidas[0]
                else:
                    new_partida = Partida(**partida)
                    new_partida.save()    
                    
                invpartidas = InvocadorPartida.objects.filter(partida__partida_id = partida.get("partida_id"), invocador_id = apid)
                inv = match.get("invocadorpartida")
                
                
                if invpartidas:
                    new_invpartida = invpartidas[0]
                else:
                    partida_new = Partida.objects.get(partida_id=partida.get("partida_id"))
                    inv["partida"] = partida_new
                    new_invpartida = InvocadorPartida(**inv)
                    new_invpartida.save() 
                
                matchs.append(new_invpartida)
            return Response({"Success": True})
        else:
            
            matchs = InvocadorPartida.objects.filter(invocador_id = apid)[:10]#.values()
            
            
            #for i in matchs:
                
                #_partida = {"id" : i.partida }
                #partida_id = i.get("partida_id")
                #serializerP = PartidaSerializer(i.partida)
                #i["partida"] = {"id" : i.partida.id}
                
    except Exception as e:
        return Response(str(e))
        return Response({"Success": False, "msg" : "Erro ao sincronizar invocador."})

    serializer = InvocadorSerializer(invocador)
    serializerIP = InvocadorPartidaSerializer(matchs, many=True)
 
    return Response({"Success": True, "invocador": serializer.data, "matchs" : serializerIP.data})


@api_view(['GET'])
def procurar(request):
    
    nome = request.GET.get("nome", "")
    
    nome = nome.replace(" ", "").lower()
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
        
    return Response({"Success": True, "invocadores": _lista})
    

    
    