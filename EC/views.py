# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from django.shortcuts import render
from db import *
from  datetime  import  *
import  time
from django.shortcuts import HttpResponse

# Create your views here.

pg1 = {'head': 'item active', 'num': '1 slide', 'title': '第一页标题', 'text': '第一页内容', 'img': 'bootstrap/images/roll1.jpg'}
pg2 = {'head': 'item', 'num': '2 slide', 'title': '第二页标题', 'text': '第二页内容', 'img': 'bootstrap/images/roll2.jpg'}
pg3 = {'head': 'item', 'num': '3 slide', 'title': '第三页标题', 'text': '第三页内容', 'img': 'bootstrap/images/roll3.jpg'}
roll = [pg1, pg2, pg3]


def get_message():
    commodity = []
    try:
        db = DataBase()
        db.get_connect()
        db.execute('use e_commerce')
        sql = 'select commodity_name, commodity_id,commodity_describe, commodity_price, commodity_unit,commodity_image from commodity_list;'
        result = db.execute(sql)
        for i in result:
            commodity.append({'name': i[0], 'id': i[1], 'describe': i[2], 'price': i[3], 'unit': i[4], 'img': i[5]})

        return commodity

    except:
        return False


def test(request):  # 测试函数
    message = {'flag': False, 'test': ''}
    if request.method == 'POST':
        phone = request.POST.get('phone', None)
        address = request.POST.get('address', None)
        id_code = request.POST.get('id_code', None)
        total_cost = request.POST.get('total_cost', None)
        id_list = request.POST.get('id_list', None)
        num_list = request.POST.get('num_list', None)
        id_list = id_list.split(',')
        num_list = num_list.split(',')

        message['flag'] = True
        message['text'] = detect_message(total_cost, phone, address, id_code)
        if not message['text']:
            if db_record(phone, address, total_cost, id_list, num_list):
                message['text'] = '下单成功，请等待商家配送。'
            else:
                message['text'] = '网络错误，请稍后重试。'

    user_commodity = get_message()
    if not user_commodity:
        message['text'] = '网络错误，请稍后重试。'

    data_dict = {'roll': roll, 'commodity': user_commodity, 'message': message}
    return render(request, 'index.html', data_dict)


def db_record(phone, address, tc, id_list, num_list):
    tc = str(tc)
    db = DataBase()
    nowtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    try:
        db.get_connect()
        db.execute('use e_commerce')
        mes = ''
        for i in range(len(num_list)):
            if num_list[i] != '0':
                mes += id_list[i]
                mes += '*'
                mes += str(num_list[i])
                mes += ','
        sql = 'insert into user_order (phone, address, client_order, total_price, status, confirm_time) values(\'%s\', \'%s\', \'%s\', \'%s\', \'0\', \'%s\');' % (phone, address, mes, tc, nowtime)
        db.execute(sql)
        db.db_commit()
        db.db_close()
        return True
    except:
        return False


def detect_message(tc, phone, address, id_code):
    re_mes = ''
    if tc == '0':
        re_mes += '您未选购任何商品\n'
    if not phone:
        re_mes += '您未填写手机号\n'
    if not address:
        re_mes += '您未填写收货地址\n'
    if not id_code:
        re_mes += '您未填写验证码\n'
    return re_mes
