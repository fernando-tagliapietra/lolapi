#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from local import *
from collections import deque
import time

class ApiHelper(object):
    
    @staticmethod    
    def consultar(url):
        
        result = requests.get(url)
        s = { "Success" : True }
        
        if result.status_code != 200:
            s =  {"Success" : False, "error" : 400}
        
        _json = result.json()
        _json.update(s)
        return result.json()
        
    @staticmethod   
    def consultarTeste(url):
        
        from requests import Request, Session

        s = Session()
        req = Request('GET',  url)
        
        prepped = s.prepare_request(req)
        
        # do something with prepped.body
        # do something with prepped.headers
        
        resp = s.send(prepped, 
            stream=True,
            verify=True,
            timeout=20)    
        return resp
        #print(resp.status_code)
                
        
        
    @staticmethod  
    def observer_request(url, proxy=None, **kwargs):
        
        s  = {"Success" : True}
        
        if not proxy:
            proxy = API_LOL_PROXY_DEFAULT
        
        args = {'api_key': RIOT_API_KEY}
        
        for k in kwargs:
            if kwargs[k] is not None:
                args[k] = kwargs[k]
        
        r = requests.get(
            'https://{proxy}.api.pvp.net/observer-mode/rest/{url}'.format(
                proxy=proxy,
                url=url
            ),
            params=args
        )
        
        limits=(RateLimit(10, 10), RateLimit(500, 600) )
        
        for lim in limits:
            lim.add_request()
            
        if r.status_code != 200:
            s =  {"Success" : False, "error" : r.status_code }    
            
        rjson = r.json()
        rjson.update(s)
        
        return rjson
      
        
    @staticmethod  
    def base_request(url, region, proxy=None, static=False, **kwargs):
        
        region = region.lower()
        
        if not proxy:
            proxy = API_LOL_PROXY_DEFAULT
        
        args = {'api_key': RIOT_API_KEY}
        
        for k in kwargs:
            if kwargs[k] is not None:
                args[k] = kwargs[k]
        
        r = requests.get(
            'https://{proxy}.api.pvp.net/api/lol/{static}{region}/{url}'.format(
                proxy= 'global' if static else proxy,
                static='static-data/' if static else '',
                region=region,
                url=url
            ),
            params=args
        )
        
        limits=(RateLimit(10, 10), RateLimit(500, 600) )
        
        if not static:
            for lim in limits:
                lim.add_request()
        
        if r.status_code != 200:
            raise Exception({"Success" : False, "error" : r.status_code })    
            
        return  r.json()
       
        
class RateLimit:
    def __init__(self, allowed_requests, seconds):
        self.allowed_requests = allowed_requests
        self.seconds = seconds
        self.made_requests = deque()

    def __reload(self):
        t = time.time()
        while len(self.made_requests) > 0 and self.made_requests[0] < t:
            self.made_requests.popleft()

    def add_request(self):
        self.made_requests.append(time.time() + self.seconds)

    def request_available(self):
        self.__reload()
        return len(self.made_requests) < self.allowed_requests        
