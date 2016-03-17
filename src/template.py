from unit import JsonRespone

class WechatTemplate:
    def __init__(self,accessToken):
        self._accessToken = accessToken
        self._getTemplateIdUrl      = "https://api.weixin.qq.com/cgi-bin/template/api_add_template?access_token=%s"%self._accessToken
        self._getTemplateListUrl    = "https://api.weixin.qq.com/cgi-bin/template/get_all_private_template?access_token=%s"%self._accessToken
        self._sendTemplateMessageUrl= "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=%s"%self._accessToken

    def getTemplateID(self,MID):
        url = self._getTemplateIdUrl
        if int(MID)<10:
            MID = "0" + MID
        data = """{
            "template_id_short": "TM000%s",
        }"""%(MID)
        return JsonRespone(url,data)

    def getTemplateList(self,templateID):
        url  = self._getTemplateListUrl
        data = ""
        return JsonRespone(url,data)

    def sendTemplateMessage(self,openID,templateID,templateUrl,data):
        url  = self._sendTemplateMessageUrl
        data = """ {
           "touser":"%s",
           "template_id":"%s",
           "url":"%s",            
           "data":%s
        }"""%(openID,templateID,templateUrl,data)
        return JsonRespone(url,data)