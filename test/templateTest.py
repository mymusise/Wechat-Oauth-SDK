#encoding:utf-8
from wechatOauth.template import WecharTemplate

tc = WecharTemplate("ACCESS_TOKEN")

data = """{
       "first": {
           "value":"66恭喜你购买成功！",
           "color":"#ee4411"
       },
       "OrderSn":{
           "value":"巧克力",
           "color":"#173177"
       },
       "OrderStatus": {
           "value":"39.8元",
           "color":"#173177"
       },
       "remark":{
           "value":"欢迎再次购买！",
           "color":"#173177"
       }
}"""

print tc.sendTemplateMessage("OPENID","TEMPLATE_ID",data)