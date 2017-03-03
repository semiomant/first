from django.shortcuts import render
from django.http import HttpResponse
#stackoverflow awnser can grow olde
import json

# Create your views here.

from datetime import datetime


def index(request):
    now = datetime.now()
    param = request.GET.get('format','')
    if ( param == 'json'):
        output = {
        'hour': now.hour,
        'minute': now.minute,
        'day':now.day
        }
        data = json.dumps(output)
        return HttpResponse(data, content_type='application/json')
    else:
        string = "Time: {now.hour}:{now.minute} Date: {now.day}.{now.month}".format(**vars())
        context = {'output': string }
        return render(request, 'mytmpl2.html', context)
