from django.shortcuts import render
from django.http import HttpResponse
from random import randint
from time import sleep
import elasticapm

@elasticapm.capture_span()
def homeTestView(request):
    sleep(randint(1,10))
    with elasticapm.capture_span('this-should-only-take-1-second'):
        sleep(1)
    return HttpResponse('Performing some random task + always one second more, to be timed by APM!')


