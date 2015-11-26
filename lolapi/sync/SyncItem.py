#!/usr/bin/env python
# -*- coding: utf-8 -*-

from local import *
import time
import datetime


from lolapi.core.ApiHelper import ApiHelper

class SyncItem:
    
    @staticmethod    
    def getItens(regiao):
        resultado = ApiHelper.base_request(API_LOL_URL_ITEM, regiao, static=True)
        return resultado.get("data", {})