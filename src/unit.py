import urllib2
import json

def JsonRespone(url,data):
    respone     = urllib2.urlopen(url,data)
    responeData = json.loads(respone.read())
    return responeData