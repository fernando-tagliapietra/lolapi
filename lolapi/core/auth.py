import sys

from django.http import HttpResponse
from django.contrib.auth.models import *
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.contrib.auth import authenticate
from django.conf import settings

from lolapi.models import *
#from api.core.errors import *

import json as simplejson

class ApiKeyAuthentication(object):

    def is_authenticated(self, request):
		return True
		"""
        alog = ApiLogs()

        auth_string = request.GET.get('API_KEY', None)

        if not auth_string:
            raiseError('auth_required', request, alog, 'falta API_KEY')
            return False

        try:
            api_user = ApiUsers.objects.get(api_key=auth_string)
            
        except:
            print sys.exc_info()
            raiseError('auth_required', request, alog, 'API_KEY invalida')
            return False

        alog.user = api_user
     	saveLog( request, alog )
        return True
		"""

    def challenge(self):
        resp = HttpResponse(simplejson.dumps( {'Success':False, 'Message':'Requer Autenticacao'}) )
        resp['WWW-Authenticate'] = "Key Based Authentication"
        resp.status_code = 401
        return resp
