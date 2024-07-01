# -*- coding: utf-8 -*-
# @Time : 2024/5/19 15:51
# @Auth : xz_official
# @File : urls.py
# @IDE : PyCharm

from django.urls import path
from . import views

urlpatterns = [
    path("list/", views.article_list)

]