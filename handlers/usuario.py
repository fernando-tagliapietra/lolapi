# -*- coding: utf-8 -*- 
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from lolapi.models import Usuario

from lolapi._serializers.UsuarioSerializer import UsuarioSerializer
from lolapi._serializers.UsuarioInfoSerializer import UsuarioInfoSerializer

from rest_framework import status

from local import *

import re
import json
#from talk.forms import PostForm

"""
@api_view(['GET'])
def usuario_collection(request):
    if request.method == 'GET':
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)
"""

@api_view(['GET'])
def usuario_element(request, pk):
    try:
        usuario = Usuario.objects.get(pk=pk)
    except Usuario.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def usuario_collection(request):
    if request.method == 'GET':
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        result = {"Success" : True, "usuarios": serializer.data }
        return Response (result)
        
    elif request.method == 'POST':
        
        email   = request.POST.get("email")
        senha   = request.POST.get("senha")
        nome    = request.POST.get("nome")
        ##regex email
        
        #raise Exception(email)
        #return Response({"e" : email, "d" : senha, "g" : nome})
        
        if not email or not senha or not nome:
            return Response({"Success": False, "msg": "Parametros obrigatorios inválidos"})
            
        if not re.match(REGEX_EMAIL, email):
            return Response({"Success": False, "msg": "E-mail Inválido"})
             
        if Usuario.objects.filter(email=email):
            return Response({"Success": False, "msg": "Email já usuário em um usuário"})
             
        if Usuario.objects.filter(nome=nome):
            return Response({"Success": False, "msg": "Nome de usuário já existente"})
            
        data = {
            'email' : email,
            'senha' : senha,
            'nome'  : nome
        }
            
        serializer = UsuarioSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"Success": True})
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET'])
def autenticar(request, info=None):
    
    nome  = request.GET.get("nome")
    email = request.GET.get("email")
    senha = request.GET.get("senha")
    
    kwargs = { "senha" : senha }
    
    if not nome and not email or not senha:
        return Response({"Success": False, "msg" : "Credenciais incomplentas"})
    
    if nome:  kwargs["nome"] = nome
    if email: kwargs["email"] = email
    
    try:
        usuario = Usuario.objects.get(**kwargs)
    except Usuario.DoesNotExist:
        return Response({"Success": False, "msg" : "Usuário não existe."})
    except Exception as e:
        return Response({"Success": False, "msg" : "Usuário/Senha Inválidos."})

    result = { "Success" : True }
    
    if info:
        serializer = UsuarioInfoSerializer(usuario)
        result["usuario"] = serializer.data
    
    return Response(result)