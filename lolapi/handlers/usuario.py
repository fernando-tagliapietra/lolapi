# -*- coding: utf-8 -*-
import json as simplejson
from piston.handler import BaseHandler
from piston.utils import rc 

#from api.core.alog import *
#from api.core.errors import *


from local import *

#import re
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist

from django.http import HttpResponse


from lolapi.models import *



class ListarHandler(BaseHandler):

	allowed_methods = ('GET')
	def read(self, request):
	    r =  HttpResponse({"Success": True}, content_type="application/x-json")
	    
	    
	    return {"Success" : True, "ddd": "dnvnao"}
        
        #usuarios	= Usuario.objects.filter()
        
        
        #return { "Success": True, "emails" : usuarios } 
        


        """
        
        if not KeyHelper.auth(request):
	     pass
            #return JsonResponse({'Success': False, 'msg': MSG_ERROR_NOT_AUTH })
        
		pagina = request.GET.get("pagina") or 1

		try:
			pagina = int(pagina)
		except Exception:
			return raiseError('param_missing', request, alog)

		total			= Email.objects.filter(ativo=1).count()
		total_paginas	= total/AASSINATURA_QTDE_LIMIT

		if total % AASSINATURA_QTDE_LIMIT:
			total_paginas += 1
		
		pointA = 0 if pagina == 1 else (AASSINATURA_QTDE_LIMIT*(pagina-1))
		pointB = AASSINATURA_QTDE_LIMIT * pagina
		
		emails		= Email.objects.filter(ativo=1).order_by("-data_criacao")[pointA:pointB]
		"""
		
		


"""
def listarUsuarios(request):

    if not KeyHelper.auth(request):
        return JsonResponse({'Success': False, 'msg': MSG_ERROR_NOT_AUTH })
    
    
    json_serializer = serializers.get_serializer("json")()
   
    
    usuarios = Usuario.objects.filter()
    
    stream = BytesIO({"resutlado" : 1})
    data = JSONParser().parse(stream)
   
    
    content = JSONParser().render(data)
    return data
    
    
    retorno = {"resultado" : usuarios}
    
    return retorno
    
    usuarios_serialized = pickle.dumps(usuarios)

   # usuarios = json_serializer.serialize(usuarios)

    #if request.is_ajax():
    #if request.method == 'GET':
        
    response = JsonResponse({
        'Success' : True,
        'usuarios': usuarios_serialized
       
    })
    
    #response.content
    return response
 
@csrf_exempt
def adicionarUsuario(request):
    email  = request.POST.get("email")
    senha  = request.POST.get("senha")
   
    if not KeyHelper.auth(request):
        return JsonResponse({'Success': False, 'msg': MSG_ERROR_NOT_AUTH })
    
    if not email or not senha:
        pass
    
    if Usuario.objects.filter(email = email):
        return JsonResponse({'Success': False, 'msg': "Usuario ja cadastrado" })
     
    #validar email
    #validar senha
    
    kwargs = { 
        "email": email,
        "senha": senha
    }
    
    usuario = Usuario(**kwargs)
    usuario.save()
    
    response = JsonResponse({'Success': True})
    return response
    
def alterarUsuario(request):
    response = JsonResponse({'Success': True})
    return response
    
def selecionarUsuario(request):
    response = JsonResponse({'Success': True})
    return response
    
def autenticarUsuario(request):
    response = JsonResponse({'Success': True})
    return response
    
    

    
"""
    
    
    
    
