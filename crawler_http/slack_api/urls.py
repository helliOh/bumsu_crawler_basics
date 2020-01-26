# -*- coding: utf-8 -*-
from django.urls import path
from django.conf.urls import include
from django.views.decorators.csrf import csrf_exempt
from slack_api import views

urlpatterns = [
    path('', csrf_exempt(views.index), name='index')
]