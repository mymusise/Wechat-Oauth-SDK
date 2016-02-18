from wechatOauth.WechatOauth import WechatOauth
from django.http import HttpResponseRedirect

def oauth(req):
    try:
        code = req.GET.get('code')
        if code:
            oauthClient = WechatOauth(code)
            if oauthClient.IsAvailable():
                openID = oauthClient.getOpenID()
            else:
                pass  # return render('req','error.html')
    except BaseException as e:
        print e