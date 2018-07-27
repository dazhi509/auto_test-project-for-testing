from django.shortcuts import render
from auto.models import AutoConfigInfos
from django.http import HttpResponse, JsonResponse
import json
import django.core.serializers as serializers

# Create your views here.

def index(request):
    print('getting index page')
    # response = {}
    # config_infos = AutoConfigInfos.objects.filter(pk=1)
    # data = json.loads(serializers.serialize("json", config_infos))
    # print(data, 'data')
    # response['test'] = data
    response = {
              "test": [
                        {
                          "num": "001",
                          "cpu": "aaa",
                          "memory": "123",
                          "disk": "dsaf",
                          "ssd": "dsfds",
                          "board": "fsd",
                          "radiator": "ewq23",
                          "chassis": "wet45",
                          "panel": "54fret",
                          "state": "rwe34"
                        },
                        {
                          "num": "002",
                          "cpu": "bbb",
                          "memory": "213",
                          "disk": "eref",
                          "ssd": "dfdgds",
                          "board": "gsdd",
                          "radiator": "ewqdfg3",
                          "chassis": "wsdf34",
                          "panel": "554ret",
                          "state": "rwe34"
                        },
                        {
                          "num": "003",
                          "cpu": "ccc",
                          "memory": "wer3",
                          "disk": "dsdff",
                          "ssd": "dwadefds",
                          "board": "f34d",
                          "radiator": "e323",
                          "chassis": "w4545",
                          "panel": "54ertreet",
                          "state": "rwewq4"
                        },
                        {
                          "num": "004",
                          "cpu": "ddd",
                          "memory": "dsf3",
                          "disk": "dsgdfgf",
                          "ssd": "dssdfs",
                          "board": "fs234",
                          "radiator": "e32423",
                          "chassis": "we5r45",
                          "panel": "5345ret",
                          "state": "rwe34"
                        },
                        {
                          "num": "006",
                          "cpu": "eee",
                          "memory": "45543",
                          "disk": "dwef",
                          "ssd": "d34rds",
                          "board": "fsdf3",
                          "radiator": "erew23",
                          "chassis": "we4455",
                          "panel": "54fret",
                          "state": "rwe34"
                        }
                      ]
                    }
    return JsonResponse(response)


def display_meta(request):
    values = request.META.items()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))


def compare(request):
    server_num = request.json().get('server_num', 1)
    oa = AutoConfigInfos.objects.filter(server_num=server_num)
    ob = AutoConfigInfos.objects.filter(server_num=server_num)
    if oa != ob:
        oa.status = False
        ob.status = False
    return HttpResponse(oa.json(), ob.json())


# def test(request):
# #     test_msg = request.POST.get('test', None)
# #     ip = request.POST.get('ip', None)
# #     port = request.POST.get('port', None)
# #
# #     client =