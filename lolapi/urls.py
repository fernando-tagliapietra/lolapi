# -*- coding: utf-8 -*- 

from django.conf.urls import patterns, include, url


urlpatterns = patterns('handlers',

    url(r'^$', 'usuario.usuario_collection'),
    url(r'^api/v1/usuarios/$', 'usuario.usuario_collection'),
    url(r'^api/v1/usuarios/(?P<pk>[0-9]+)$', 'usuario.usuario_element'),
    
    url(r'^api/v1/auth/$', 'usuario.autenticar'),
    url(r'^api/v1/auth/info/$', 'usuario.autenticar', {"info": 1}),
    
    url(r'^api/v1/invocador/listar/$', 'invocador.listar'),
    url(r'^api/v1/invocador/adicionar/$', 'invocador.adicionar'),
    url(r'^api/v1/invocador/selecionar/$', 'invocador.selecionar'),
    url(r'^api/v1/invocador/sincronizar/$', 'invocador.selecionar', {"sync" : 1}),
    
    url(r'^api/v1/invocador/procurar/$', 'invocador.procurar'),
    
    url(r'^api/v1/usuario/invocador/adicionar/$', 'usuario_invocador.adicionar', {"favorito" : 0 }),
    url(r'^api/v1/usuario/invocador/favorito/$', 'usuario_invocador.adicionar', {"favorito" : 1 }),
    
    url(r'^api/v1/campeao/listar/$', 'campeao.listar'),
    url(r'^api/v1/campeao/sincronizar/$', 'campeao.sincronizar'),
    
    url(r'^api/v1/item/listar/$', 'item.listar'),
    url(r'^api/v1/item/sincronizar/$', 'item.sincronizar'),
    
    url(r'^api/v1/build/listar/$', 'build.listar'),
    url(r'^api/v1/build/adicionar/$', 'build.adicionar'),

    # Examples:
    # url(r'^$', 'lolapi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^admin/', include(admin.site.urls)),
)


"""
from django.conf.urls import patterns, include, url
#from django.contrib import admin

from piston.resource import Resource

from lolapi.handlers import usuario

from lolapi.core.auth import ApiKeyAuthentication


_api_key_auth = ApiKeyAuthentication()

class APIProtectedResource( Resource ):

    def __init__( self, handler, authentication = _api_key_auth):
		
		authentication.handler = handler
		super( APIProtectedResource, self ).__init__( handler, authentication )
		self.csrf_exempt = getattr( handler, 'csrf_exempt', True)

#from admin import *
APR = APIProtectedResource 


'''

import json as simplejson
from lolapi.handlers import teste

#from django.conf.urls import *  
from django.conf.urls import patterns, include, url
#from django.conf.urls.defaults import *
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication

auth = HttpBasicAuthentication(realm="My Realm")
ad = { 'authentication': auth }

blogpost_resource = Resource(handler=teste.ListarHandler, **ad)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lolapi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
  
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^usuario/listar/', blogpost_resource ),
    
    
    
)

"""
