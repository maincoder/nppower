import json, time, os
from urllib import request as rqt
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import redis
import base64

conn = redis.Redis(host='127.0.0.1',port=6379)

@csrf_exempt 
def create_session(request):
    if request.method == 'GET':
        #data = request.POST
        randstr = str(base64.b64encode(os.urandom(96)),encoding ='utf-8')
        print(randstr)
        js_code = request.GET.get('code') 
        url =  'https://api.weixin.qq.com/sns/jscode2session?appid=wx08127c4692d58a6b&secret=d0cc0879dfbc27df51616bed3e6b8fd0&grant_type=authorization_code'
        url = url + "&js_code=" + js_code 
        response = rqt.urlopen(url)
        page = str(response.read(),encoding = 'utf-8')
        page_dict = json.loads(page)
        print(page_dict)
        v = page_dict['openid']
        conn.set(randstr,v)
        conn.expire(randstr, 12 * 60 * 60)
        resp = HttpResponse(json.dumps({'my_session':randstr}), content_type='application/json')
        resp['errcode'] = 0
        return resp

