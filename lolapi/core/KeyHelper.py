# -*- coding: utf-8 -*- 
from local import *

class KeyHelper:
    
    @staticmethod
    def auth(request):
        
        key = request.GET.get("API_KEY")
            
        if key in API_KEY:
            return True
            
        return False
            
            
        