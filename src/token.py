from unit import JsonRespone

class WechatToken:
    def __init__(self,APP_ID,APP_SECRET_KEY):
        self._get_access_token_url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s"%(APP_ID,APP_SECRET_KEY)
        self._access_token = self._get_access_token()
        

    def _get_access_token(self):
        url  = self._get_access_token_url
        data = ""
        return JsonRespone(url,data)['access_token']

    @property
    def get_access_token(self):
        return self._access_token
