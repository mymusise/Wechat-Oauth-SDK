wechat-oauth
===

一个Python封装微信公共平台SDK，目前功能包括

- OAuth登陆API 

- 以及部分WEB服务器主动消息API


##安装

####pip源安装

```
pip install wechatOauth
```

####源码安装
```
python setup.py install 
```


##Oauth接口功能

目前只有微信的网页oauth静默登陆，就是不需要点击授权来获取微信用户的OPENID。
后续加上snsapi_userinfo类型的接口。


###Django例子
```
from wechatOauth.WechatOauth import WechatOauth

def oauth(req):
    try:
        code = req.GET.get('code')
        if code:
            oauthClient = WechatOauth("APP_ID","APP_SECRET_KEY",code)
            if oauthClient.IsAvailable():
                openID = oauthClient.getOpenID()
                pass  # do something and return your web page
            else:
                pass  # return render('req','error.html')
    except BaseException as e:
        print e
```

- oauth是django的一个view,在redirect_uri参数中应该要返回oauth这个view对应的url。

- 初始化WechatOauth的时候需要你的公众号AppID和AppSecret和一个code。

- code是微信ouath认证返回过来的代码。

- getOpenID()返回某用户对某公众号的OPENID。

更多参数解析详见：[官方文档](http://mp.weixin.qq.com/wiki/4/9ac2e7b1f1d22e9e57260f6553822520.html)


##其他API

###服务器主动消息API

微信官方文档：[客服消息](http://mp.weixin.qq.com/wiki/11/c88c270ae8935291626538f9c64bd123.html) ， [模板消息](http://mp.weixin.qq.com/wiki/5/6dde9eaa909f83354e0094dc3ad99e05.html)

####wechatOauth.customer.WechatCustomer

用于客服消息发送

- 初始化 **WechatCustomer(ACCESS_TOKEN)**

- 函数 sendTextMessage：
  - 描述：主动向用户发送文本消息
  - 参数：[openID]（String）， [context]（String）
  - 返回：JSON代码

- 函数 sendImageMessage：
  - 描述：主动向用户发送图片消息
  - 参数：[openID]（String）， [mediaID]（String）
  - 返回：JSON代码

- 函数 sendSingleArticlesMessage：
  - 描述：主动向用户发送一条图文消息，（注意是一条！微信原接口最多一次发送8条，后期实现）
  - 参数：[openID]（String）， [articles]（Dirt）
  - 返回：JSON代码


####wechatOauth.media.WechatMedia

获取素材信息，辅助 **WechatCustomer** 的图文接口

- 初始化 **WechatMedia(ACCESS_TOKEN)**

- 函数 getMediaIdList：
  - 描述：获取素材ID列表
  - 参数：[type]（String）， [offset]（Integer）， [count]（Integer）
  - 返回：JSON代码


####wechatOauth.template.WechatTemplate

发送模板消息

- 初始化 **WechatTemplate(ACCESS_TOKEN)**

- 函数 getTemplateID：
  - 描述：通过MID来获取完整的TemplateID
  - 参数：[MID]（String）
  - 返回：JSON代码

- 函数 getTemplateList：
  - 描述：获取Template列表
  - 参数：空
  - 返回：JSON代码

- 函数 sendTemplateMessage：
  - 描述：发送Template模板内容给用户
  - 参数：[openID]（String）， [templateID]（String）,[templateUrl](Sting)，[data]（String）
  - 返回：JSON代码



##叨叨一下
只拿到openid有什么卵用，，，
这样用户在点开你的微信网站应用时候就不需要登陆，你就知道来者何人了

## 交流

- 直接mail作者：mymusise1@gmail.com

- 或者加我微信：mymusise


## License
The MIT license.