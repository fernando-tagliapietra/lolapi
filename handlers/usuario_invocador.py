# -*- coding: utf-8 -*- 
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from lolapi.models import Invocador, Usuario, UsuarioInvocador
from lolapi._serializers.InvocadorSerializer import InvocadorSerializer
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from rest_framework import status


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
def adicionar(request, favorito=0):
    
        usuario_nome        = request.POST.get("usuario_nome")
        invocador_riot_id   = request.POST.get("invocador_id")
    
        if not usuario_nome or not invocador_riot_id:
            return Response({"Success" : False, "msg" : "Parametros Inválidos"})
            
        try:
            invocador_id = int(invocador_riot_id)
        except Exception as e:
            return Response({"Success" : False, "msg" : "RIOT ID inválido"})
        
        try:
            usuario = Usuario.objects.get(nome=usuario_nome)
        except MultipleObjectsReturned as mor:
            return Response({"Success" : False, "msg" : "Mais de um usuario retornado"})
        except ObjectDoesNotExist as one:
            return Response({"Success" : False, "msg" : "Usuário não existe"})
        except Exception as e:
            return Response({"Success" : False, "msg" : str(e)})
        
        try:
            invocador = Invocador.objects.get(api_id = invocador_riot_id)
        except MultipleObjectsReturned as mor:
            return Response({"Success" : False, "msg" : "Mais de um invocador retornado"})
        except ObjectDoesNotExist as one:
            return Response({"Success" : False, "msg" : "Invocador não existe"})
        except Exception as e:
            return Response({"Success" : False, "msg" : str(e)})
            
        ui = UsuarioInvocador(invocador = invocador, usuario = usuario, favorito = favorito)
        
        try:
            ui.save()
        except Exception as e:
           return Response({"Success" : False, "msg" : "Erro ao adicionar o invocador ao usuario"})
        
        return Response({"Success": True})