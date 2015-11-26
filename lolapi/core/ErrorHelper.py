# -*- coding: utf-8 -*- 

from lolapi.models import *
from django.http import JsonResponse


class ErrorHelper:
    
    @staticmethod
    def getError(code):
        
        try:
            msg = Mensagem.objects.get(codigo = code)
        
        
            return JsonResponse({
                "Success": False, 
                "msg"    : msg.mensagem
            })
            
        except:
            pass
            
    