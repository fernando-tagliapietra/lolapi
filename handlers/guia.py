# -*- coding: utf-8 -*- 
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from lolapi.models import Guia, Usuario
from lolapi._serializers.GuiaSerializer import GuiaSerializer

import datetime
        
@api_view(['GET'])
def listar(request):
    
    kwargs = {}
    campeao_id = request.GET.get("campeao_id")
    
    if campeao_id:
        kwargs["campeao__id"] = campeao_id
     
    try: 
        campeao = Campeao.objects.get(id=campeao_id)    
    except Exception as e:
        return Response ({"Success": False, "msg" : str(e) })
        
    builds = Build.objects.filter(**kwargs)
    serializer = BuildSerializer(builds, many=True)
    c_serializer = CampeaoSerializer(campeao)
    result = {"Success" : True, "builds": serializer.data, "campeao" : c_serializer.data }
    return Response (result)


@api_view(['POST'])
def adicionar(request):
    
        descricao    = request.POST.get("descricao")
        magia1       = request.POST.get("magia1")
        magia2       = request.POST.get("magia2")
        usuario_id   = request.POST.get("usuario_id")
        campeao_id   = request.POST.get("campeao_id")
        temporada    = request.POST.get("temporada")
        
        
        item1 = request.POST.get("item1")
        item2 = request.POST.get("item2")
        item3 = request.POST.get("item3")
        item4 = request.POST.get("item4")
        item5 = request.POST.get("item5")
        
        lista_itens = [item1, item2, item3, item4, item5]
        
        
        if not all([descricao, usuario_id, campeao_id]):
            return Response({"Success": False, "msg": "Parametros obrigatorios inválidos"})
        
        try:
            usuario = Usuario.objects.get(id = usuario_id)
            campeao = Campeao.objects.get(id = campeao_id)
        except Exception as e:
            return Response({"Success": False, "msg": "Erro ao buscas usuario"})
        
        
        data_build = {
            'descricao': descricao,
            'magia1': magia1,
            'magia2': magia2,
            'usuario' : usuario,
            'campeao': campeao,
            'temporada': temporada,
        }
            
        try:
            build = Build(**data_build)
            build.save()
        except Exception as e:
            return Response({"Success": False, "msg": "Erro ao salvar build"})
            
        for item_id in lista_itens:
            item = Item.objects.get(item_id = item_id)
            
            bi = BuildItem(build = build, item=item)
            bi.save()
            
        return Response({"Success": True}, status=200)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
@api_view(['POST'])
def selecionar(request, sync=None):
    
    apid        = request.POST.get("apid")
    regiao      = request.POST.get("regiao")
    matchs = []
   
    if not apid or not regiao:
        return Response({"Success": False, "msg": "Parametros obrigatorios inválidos"})
    
    invocadores = Invocador.objects.filter(api_id=apid)
    
    try:
        
        if invocadores and not sync:
            invocador = invocadores[0]   
        else:
            dados_invocador = SyncSummoner.getSummoner(apid, regiao)
            
            if sync and invocadores:
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
    

    
    