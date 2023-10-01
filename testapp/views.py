import glob
import json
import os
from datetime import datetime

from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

from testapp.models import EntityTexture


def texture_gallery(request):
    base_dir = str(settings.BASE_DIR / 'static').replace(os.sep, '/') + '/'
    file_abs_paths = glob.glob(str(settings.BASE_DIR / 'static/monsters/**/*.png'))
    for file_abs_path in file_abs_paths:
        file_path = file_abs_path.replace(os.sep, '/').split(base_dir)[1]
        category = file_path.split('/')[0]
        sub_category = file_path.split('/')[1]
        code = file_path.split('/')[2].split('.png')[0]
        entity_texture = EntityTexture.objects.get_or_create(
            category=category,
            sub_category=sub_category,
            code=code,
        )
        print(entity_texture)

    entity_textures = EntityTexture.objects.all()
    context = {'entity_textures': entity_textures}
    return render(request, 'testapp/texture_gallery.html', context)


def save(request, code, name):
    e = EntityTexture.objects.get(code=code)
    e.name = name
    e.save()
    return JsonResponse({'status': 'OK'})
