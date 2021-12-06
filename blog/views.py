from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def say_hello(request):
    return HttpResponse('Hello Teacher')


def registration(request):
    a = 'Please give me 10'
    return HttpResponse(a)


def gratitude(request):
    b = 'Thanks'
    return HttpResponse(b)
