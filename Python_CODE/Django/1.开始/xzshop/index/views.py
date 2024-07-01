from django.shortcuts import render
from django.http import HttpResponse


# views.py: 视图,写应用逻辑的
def hello(request):
    return HttpResponse("你好!这是首页")


def big(request):
    return HttpResponse("yes good!")
