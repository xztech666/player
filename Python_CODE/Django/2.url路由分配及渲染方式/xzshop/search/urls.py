# -*- coding: utf-8 -*-
# @Time : 2024/5/12 16:34
# @Auth : xz
# @File : urls.py
# @IDE : PyCharm

from django.urls import path, re_path
from . import views

urlpatterns = [
    # path('<str:kw>', views.search),
    re_path('(?P<kw>\w{4,}$)', views.search)
]
