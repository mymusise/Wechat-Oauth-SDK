from wechatOauth.customer import WechatCustomer

c = WechatCustomer("ACCESS_TOKEN")

print c.sendTextMessage("OPENID","TEXT")