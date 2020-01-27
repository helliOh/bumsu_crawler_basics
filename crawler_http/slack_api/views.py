# -*- coding: utf-8 -*-
import datetime
import requests
import json

from django.http import JsonResponse, HttpResponse
from slack import WebClient

from .commands.handler import Command

# list commands
def eventHandler(eventType, data):
    if eventType == "app_mention":
        channel = data["event"]["channel"]
        message = Command.handle(data)
        return JsonResponse(
                message,
                json_dumps_params={'ensure_ascii': False},
                content_type="application/json; encoding=utf-8",
                safe=False
            )
   
    message = "[%s] 이벤트 핸들러를 찾을 수 없습니다." % eventType

    return HttpResponse(message, status=200)

def index(request):
    # event handler
    res = ''
    body = ''
    command = ''

    if len(request.body) > 1:
        body = json.loads(request.body)

        if "challenge" in body:
            return JsonResponse(
                body,
                json_dumps_params={'ensure_ascii': False},
                content_type="application/json; encoding=utf-8",
                safe=False
            )
        if "event" in body:
            eventType = body['event']['type']
            return eventHandler(eventType, body)
    else :
        return HttpResponse(status=404)

    

    



    


