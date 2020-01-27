# -*- coding: utf-8 -*-
import datetime
import requests
import json

from django.http import JsonResponse, HttpResponse
from slack import WebClient

token = 'YOUR BOT TOKEN'
channelName = 'YOUR DEFAULT CHANNEL'

with open("config/env.json", "r") as st_json:
    env = json.load(st_json)
    token, channelName = env["SLACK_BOT_TOKEN"], env["SLACK_DEFAULT_CHANNEL"]

def sendMessage(data):
    client = WebClient(token=token)
    response = client.chat_postMessage(channel=channelName, text=data)

    return data

class Greeting:
    def echo(greeting):
        return sendMessage(greeting)

        