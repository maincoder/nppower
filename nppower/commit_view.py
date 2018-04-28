import json, time, redis
from .models_mongo import RaceWx
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt

#todo conn pool
conn = redis.Redis(host='127.0.0.1',port=6379)

@csrf_exempt
def post_race(request):
    if request.method == 'POST':
        data = request.POST
        print(data)
        my_session = data.get('my_session')
        print(my_session)
        ret_datas = []
        openId = conn.get(my_session)
        if openId:
            openId = str(openId, encoding='utf-8')
        else:
            return HttpResponse(json.dumps({'errcode':-1}),content_type="application/json")
        print("cached openid:"+openId) 
        rt = data.get('racetime')
        timeArray = time.strptime(rt, "%Y-%m-%d %H:%M")
        tstamp = 1000 * time.mktime(timeArray)
        
        RaceWx.objects.create(name= data.get("name"),time=tstamp,openid=openId)
        ret = {"errcode":0}
        return HttpResponse(json.dumps(ret), content_type='application/json')

@csrf_exempt 
def delete_race(request):
    if request.method == 'POST':
        data = request.POST
        racetime = data.get('racetime')
        my_session = data.get('my_session')
        print(my_session)
        ret_datas = []
        openId = conn.get(my_session)
        if openId:
            openId = str(openId, encoding='utf-8')
        else:
            return HttpResponse(json.dumps({'errcode':-1}),content_type="application/json")
        print("cached openid:"+openId) 
        RaceWx.objects.filter(time=racetime,openid=openId).delete()
        ret = {"errcode":0}
        return HttpResponse(json.dumps(ret), content_type='application/json')


@csrf_exempt 
def api_get_racelist(request):
    if request.method == 'GET':
        data = request.GET
        my_session = data.get('my_session')
        if my_session:
            my_session = my_session.replace('%2F','/').replace("%3D","=").replace("%2B","+") 
            print("myss:"+my_session)
        else:
            print("empty myss")
        ret_datas = []
        openId = conn.get(my_session)
        flag = 0
        if openId:
            openId = str(openId, encoding='utf-8')
            print("openid:"+openId)
        else:
            resp =  HttpResponse(json.dumps({'errcode':-1}),content_type="application/json")
            return resp
        print("cached openid:"+openId) 
        pre_time = (int(round(time.time() * 1000)))  
        
        for data in RaceWx.objects(openid=openId).order_by('time'):
            ret_data = {}
            ret_data['date'] = time.strftime("%Y-%m-%d %H:%M", time.localtime(data.time/1000))  
            ret_data['name'] = data.name
            ret_data['time'] = data.time
            ret_data['inter'] = data.time - pre_time
            pre_time = data.time
            ret_datas.append(ret_data)
        print(ret_datas)
        resp =  HttpResponse(json.dumps({'data':ret_datas,'errcode':0}),content_type="application/json")
        return resp





