#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from django.template import Context, Template, loader, RequestContext

from django.http import HttpResponse, HttpResponseRedirect
import json as simplejson

#import pycurl
import StringIO
import urllib
import urllib2

import json
import requests

from datetime import datetime
from local import *

BAD_GATEWAY = 500
HTTP_SUCCESS = 200

def api_get(url, params):

	r = requests.get( '{url}'.format( url=url ), params=params )
	
	s = {}
	
	if r.status_code != HTTP_SUCCESS:
		s =  {"Success" : False, "error" : r.status_code }
		
	rjson = r.json()
	rjson.update(s)
	return rjson


def api_post(url, api_key, params):
	
	r = requests.post(url, params={"api_key" : api_key} , data=params)
	
	s = {}
	
	if r.status_code != HTTP_SUCCESS:
		s =  {"Success" : False, "error" : r.status_code }
		
	rjson = r.json()
	rjson.update(s)
	return rjson