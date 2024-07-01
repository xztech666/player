from django.shortcuts import render
from django.http import HttpResponse


def search(request, kw):
    return HttpResponse("搜索:  " + kw)
