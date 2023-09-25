import json
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render


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


def gallery(request):
    return render(request, 'testapp/gallery.html')


def gallery_photo(request, photo):
    context = {'photo': photo}
    return render(request, 'testapp/gallery_photo.html', context)
