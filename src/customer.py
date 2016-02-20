from  unit import JsonRespone

class WechatCustomer:
    def __init__(self,accessToken):
        self._accessToken = accessToken
        self._messageUrl  = "https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token=%s"%self._accessToken

    def sendTextMessage(self,openID,context):
        url = self._messageUrl
        data = """{
            "touser": "%s", 
            "msgtype": "text", 
            "text": {
                "content": "%s"
            }
        }"""%(openID,context)
        return JsonRespone(url,data)

    def sendImageMessage(self,openID,mediaID):
        url = self._messageUrl
        data = """{
            "touser": "%s", 
            "msgtype": "image", 
            "image": {
                "media_id": "%s"
            }
        }"""%(openID,mediaID)
        return JsonRespone(url,data)

    def sendSingleArticlesMessage(self,openID,articles):
        url = self._messageUrl
        data = """{
            "touser":"%s",
            "msgtype":"news",
            "news":{
                "articles": [
                 {
                     "title":"%s",
                     "description":"%s",
                     "url":"%s",
                     "picurl":"%s"
                 }
                 ]
            }
        }"""%(openID,
                articles['title'],
                articles['description'],
                articles['url'],
                articles['picurl'],
            )
        return JsonRespone(url,data)

    def getAccessToken(self):
        return self._accessToken

    def getMessageRequestUrl(self):
        return self._messageUrl
