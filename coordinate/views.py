import random
from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Transfer
import simplejson as simplejson
from .pushmessage import push_normal_message, push_tencent_message
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return HttpResponse("index")


@csrf_exempt
def add_share(request):
    result_dict = {}
    share_pin = None
    try:
        if request.method == 'POST':
            req = simplejson.loads(request.body)
            origin_phone = req['origin_phone']
            token = req['token']
            data_type = req['data_type']
            related_data = req['related_data']
            ip = req['ip']
            port = req['port']
            installation = req['installation']
            pin_code = random.randint(1000, 9999)
            while True:
                try:
                    db_pin = Transfer.objects.filter(is_active=True).get(share_pin=pin_code)
                    pin_code = random.randint(1000, 9999)
                except Transfer.DoesNotExist:
                    break
            share_pin = pin_code
            new_transfer = Transfer(origin_phone=origin_phone, token=token, data_type=data_type,
                                    related_data=related_data, ip=ip, port=port, share_pin=share_pin,
                                    installation_origin=installation, is_active=True)
            new_transfer.save()
    except Exception as ex:
        print(ex)
        raise Http404
    result_dict['status'] = 'success'
    result_dict['pin'] = share_pin
    json = simplejson.dumps(result_dict)
    return HttpResponse(json)


@csrf_exempt
def get_share(request):
    result_dict = dict()
    try:
        if request.method == 'POST':
            req = simplejson.loads(request.body)
            pin_code = req['pin_code']
            installation = req['installation']
            obj2transfer = Transfer.objects.filter(is_active=True).get(share_pin=pin_code)
            obj2transfer.installation_target = installation
            obj2transfer.save()
            result_dict['status'] = 'success'
            result_dict['id'] = obj2transfer.id
            result_dict['origin_phone'] = obj2transfer.origin_phone
            result_dict['token'] = obj2transfer.token
            result_dict['data_type'] = obj2transfer.data_type
            result_dict['related_data'] = obj2transfer.related_data
            result_dict['ip'] = obj2transfer.ip
            result_dict['port'] = obj2transfer.port
    except:
        raise Http404
    json = simplejson.dumps(result_dict)
    return HttpResponse(json)


@csrf_exempt
def connect_error(request, transfer_id):
    transfer = Transfer.objects.get(pk=transfer_id)
    message_title = "与对方手机未能建立近距离连接"
    message_content = "请选择是否通过云服务传输"
    push_normal_message(transfer.installation_origin, message_title, message_content)
    return HttpResponse("success")
