from  unit import JsonRespone

class WechatMedia:
    def __init__(self,accessToken):
        self._accessToken = accessToken
        self._listUrl  = "https://api.weixin.qq.com/cgi-bin/material/batchget_material?access_token=%s"%self._accessToken

    def getMediaIdList(self,type,offset,count):
        url = self._listUrl
        data = """{
            "type": "%s", 
            "offset": %d, 
            "count" : %d
        }"""%(type,offset,count)
        return JsonRespone(url,data)
