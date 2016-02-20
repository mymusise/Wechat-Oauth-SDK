import urllib2
import json

class WechatOauth:
    def __init__(self,APP_ID,APP_SECRET_KEY,code):
        self.data  = {}
        self._APP_ID = APP_ID
        self._APP_SECRET_KEY = APP_SECRET_KEY
        if self.getTokenByCode(APP_ID,APP_SECRET_KEY,code):
            self.__is_available = True
        else:
            self.__is_available = False

    def getParameter(self,url):
        req = urllib2.urlopen(url)
        self.data = json.loads(req.read())
        if self.data.get('errcode'):
            return False
        else:
            return True

    def getTokenByCode(self,appid,secret,code):
        url = """https://api.weixin.qq.com/sns/oauth2/access_token?appid=%s&secret=%s&code=%s&state=123&grant_type=authorization_code""" % (appid,secret,code)
        if self.getParameter(url):
            self.__token     = self.data['access_token']
            self.__openID    = self.data['openid']
            # self.__unionID   = self.data['unionid']
            return True
        else:
            return False

    def getToken(self):
        return self.__token

    def getOpenID(self):
        return self.__openID

    def getUnionID(self):
        return self.__unionID

    def IsAvailable(self):
        if self.__is_available:
            return True
        else:
            return False