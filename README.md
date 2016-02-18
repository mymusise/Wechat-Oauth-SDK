wechat-oauth
===

一个Python封装的微信公共平台OAuth登陆API SDK


##安装

####pip源安装

```
pip install wechatOauth
```

####源码安装
```
python setup.py install 
```


##接口功能

目前只有微信的网页oauth静默登陆，就是不需要点击授权来获取微信用户的OPENID。
后续加上snsapi_userinfo类型的接口。


##Django例子
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


##叨叨一下
只拿到openid有什么卵用，，，
这样用户在点开你的微信网站应用时候就不需要登陆，你就知道来者何人了

## 交流

- 直接mail作者：mymusise1@gmail.com

- 或者加我微信：mymusise


## License
The MIT license.