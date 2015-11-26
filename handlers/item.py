# -*- coding: utf-8 -*- 
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from lolapi.models import Item
from lolapi._serializers.ItemSerializer import ItemSerializer
from lolapi.sync.SyncItem import SyncItem


@api_view(['GET'])
def listar(request):

    kwargs = {}
    procura = request.GET.get("procura")
    
    if procura:
        kwargs["nome__contains"] = procura
    
    itens = Item.objects.filter(**kwargs)
    serializer = ItemSerializer(itens, many=True)
    result = {"Success" : True, "itens": serializer.data }
    return Response (result)

@api_view(['POST'])
def sincronizar(request):
    
    _items = SyncItem.getItens("BR")
    erros = 0
    
    for k, v in _items.items():
        
        item_id = v.get("id")
        
        if Item.objects.filter(item_id = item_id):
            continue
        
        item = Item(item_id=item_id, nome=v.get("name"), descricao=v.get("description"))
        
        try:
            item.save()
        except Exception as e:
            erros += 1
        
    return Response({"Success" : True, "erros" : erros})