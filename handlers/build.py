# -*- coding: utf-8 -*- 
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from lolapi.models import Build, BuildItem, Usuario, Campeao, Item
from lolapi._serializers.BuildSerializer import BuildSerializer
from lolapi._serializers.CampeaoSerializer import CampeaoSerializer

from rest_framework import status

from lolapi.core.SummonerHelper import *
from lolapi.sync.SyncSummoner import *

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
        
