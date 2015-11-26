# -*- coding: utf-8 -*- 
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from lolapi.models import Campeao
from lolapi._serializers.CampeaoSerializer import CampeaoSerializer
from lolapi.sync.SyncCampeao import SyncCampeao


@api_view(['GET'])
def listar(request):

    kwargs = {}
    procura = request.GET.get("procura")
    
    if procura:
        kwargs["nome__contains"] = procura
    

    campeoes = Campeao.objects.filter(**kwargs)
    serializer = CampeaoSerializer(campeoes, many=True)
    result = {"Success" : True, "campeoes": serializer.data }
    return Response (result)

@api_view(['POST'])
def sincronizar(request):
    
    campeoes_atualizados = SyncCampeao.getCampeoes("BR")
    erros = 0
    
    for k, v in campeoes_atualizados.items():
        
        champ_id = v.get("id")
        
        if Campeao.objects.filter(campeao_id = champ_id):
            continue
        
        campeao = Campeao(campeao_id=champ_id, nome=v.get("name"))
        
        try:
            campeao.save()
        except Exception as e:
            erros += 1
        
        
    return Response({"Success" : True, "erros" : erros})