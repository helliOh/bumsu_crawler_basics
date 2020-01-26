# -*- coding: utf-8 -*-
import datetime
import requests
import json

from django.http import JsonResponse, HttpResponse
from slack import WebClient

token = "너의 봇 토큰"
channelName = "#web-based-services"

def sendMessage(data):
    client = WebClient(token=token)
    response = client.chat_postMessage(channel=channelName, text=data)

    return data

class Greeting:
    def echo(greeting):
        return sendMessage(greeting)

        