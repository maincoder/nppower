from mongoengine import *

connect("gdp")

class Gdp(Document):
    province = StringField(max_length=50)
    rank = IntField(required=False)
    gdp_cny = FloatField(decimal_places=2)
    gdp_usd = FloatField(decimal_places=2)  
    growth = FloatField(decimal_places=1)
    share = FloatField(decimal_places=2)

    meta = { 'collection': 'province'} 

class Race(Document):
    time = LongField(required=False) 
    name = StringField(max_length = 50)    
    openid = StringField(max_length = 80)    
    meta = {'collection':'race_day'}


class RaceWx(Document):
    time = LongField(required=False) 
    name = StringField(max_length = 50)    
    openid = StringField(max_length = 80)    
    meta = {'collection':'race_wx'}
#for gdp in Gdp.objects[:10]: # 测试是否连接成功 
#    print(gdp)

