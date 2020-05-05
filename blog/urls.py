#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    :2020/5/4 18:28
# @Author  :zhouyuyao
# @File    :urls.py

from django.contrib import admin
from django.urls import path, include, re_path

from . import views



urlpatterns = [
    path('', views.index),
    # artical_id 需和 views 中 artical_page 参数保持一致
    path('artical/<int:artical_id>', views.artical_page,name='artical_page'),
    path('edit/<int:artical_id>', views.edit_page,name='edit_page'),
    path('edit/action/', views.edit_action,name='edit_action'),

]

