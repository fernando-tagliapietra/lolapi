from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from lolapi.models import Usuario

from lolapi.handlers.teste import UsuarioSerializer

from rest_framework import status


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
        return Response(serializer.data)
        
    elif request.method == 'POST':
        fields = ('id', 'nome',  'email', 'senha', 'conta_twitch', 'conta_facebook', 'conta_twitter', 'dias_jogo', 'horarios_jogo')
        
        data = {
            'nome' : request.POST.get("nome"),
            'email': request.POST.get("email"),
            'senha': request.POST.get('senha'),
            'conta_twitch': request.POST.get('conta_twitch'),
            'conta_facebook': request.POST.get('conta_facebook'),
            'conta_twitter': request.POST.get('conta_twitter'),
            'dias_jogo': request.POST.get('dias_jogo'),
            'horarios_jogo': request.POST.get('horarios_jogo'),
        }
            
        serializer = UsuarioSerializer(data=data)
        
      
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       