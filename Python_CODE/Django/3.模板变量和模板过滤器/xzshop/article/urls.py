# -*- coding: utf-8 -*-
# @Time : 2024/5/19 13:42
# @Auth : xz
# @File : urls.py
# @IDE : PyCharm

from django.urls import path
from . import views

urlpatterns = [
    path("<int:article_id>", views.detail)

]