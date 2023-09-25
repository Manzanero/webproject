import json
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def get_example(request):
    response = "hola"
    return JsonResponse(response, safe=False, json_dumps_params={'indent': 2})


@csrf_exempt
def post_example(request):
    ayb = json.loads(request.body.decode())
    a = ayb["a"]
    b = ayb["b"]
    response = int(a) + int(b)

    return JsonResponse(response, safe=False, json_dumps_params={'indent': 2})