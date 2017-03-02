from django.shortcuts import render

# Create your views here.

from datetime import datetime


def index(request):
    now = datetime.now()
    str = "Time: {now.hour}:{now.minute} Date: {now.day}.{now.month}".format(**vars())
    context = {'output': str }
    return render(request, 'mytmpl2.html', context)
