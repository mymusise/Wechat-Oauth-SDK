from wechatOauth.oauth import WechatOauth
from django.http import HttpResponseRedirect

def oauth(req):
    try:
        code = req.GET.get('code')
        if code:
            oauthClient = WechatOauth("APP_ID","APP_SECRET_KEY",code)
            if oauthClient.IsAvailable():
                openID = oauthClient.getOpenID()
            else:
                pass  # return render('req','error.html')
    except BaseException as e:
        print e