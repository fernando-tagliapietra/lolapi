#!/usr/bin/env python
# -*- coding: utf-8 -*-

from local import *
import time
import datetime


from lolapi.core.ApiHelper import ApiHelper

class SyncCampeao:
    
    @staticmethod    
    def getCampeoes(regiao):
        resultado = ApiHelper.base_request(API_LOL_URL_CHAMPION, regiao, static=True)
        return resultado.get("data", {})
    @staticmethod
    def getCampeao(id, regiao):
        url = "{url_champ}/{id}".format(url_champ=API_LOL_URL_CHAMPION, id=id)
        return ApiHelper.base_request(url, regiao)
        