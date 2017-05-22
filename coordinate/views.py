import random
from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Transfer
import simplejson as simplejson


def index(request):
    return HttpResponse("index")


def add_share(request):
    result_dict = {}
    share_pin = None
    try:
        if request.method == 'POST':
            req = simplejson.loads(request.raw_post_data)
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
            new_transfer = Transfer(origin_phone=origin_phone, token=token, data_type= data_type,
                                    related_data=related_data, ip=ip, port=port, share_pin=share_pin,
                                    installation_origin=installation)
            new_transfer.save()
    except:
        raise Http404
    result_dict['status'] = 'success'
    result_dict['pin'] = share_pin
    json = simplejson.dumps(result_dict)
    return HttpResponse(json)


def get_share(request, share_pin):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % share_pin)


def connect_unavailable(request, transfer_id):
    return HttpResponse("You're voting on question %s." % transfer_id)
