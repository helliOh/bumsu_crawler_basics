# -*- coding: utf-8 -*-
import re
import datetime
from slack import WebClient

from .menu import Menu
from .greeting import Greeting

def onFail(message):
    token = 'YOUR BOT TOKEN'
    channelName = 'YOUR DEFAULT CHANNEL'

    with open("config/env.json", "r") as st_json:
        env = json.load(st_json)
        print(env)
        token, channelName = env["SLACK_BOT_TOKEN"], env["SLACK_DEFAULT_CHANNEL"]



    print(token)
    print(channelName)
    client = WebClient(token)
    client.chat_postMessage(channel=channelName, text=message)

    return {
        'message' : 'command not found',
        'error' : 404
    }

class Command:
    def handle(data):
        print(data)
        command = data['event']['text']
        
        if "오늘 메뉴" in command:
            return Menu.todayMenu()
        elif "내일 메뉴" in command:
            return Menu.tomorrowMenu()
        elif "이 날 메뉴" in command:
            regexes = [
                re.compile(r'(?P<year>\d{4})년(?P<month>\d{2})월(?P<day>\d{2})일'),
                re.compile(r'(?P<year>\d{4})년(?P<month>\d{2})월(?P<day>\d{1})일'),
                re.compile(r'(?P<year>\d{4})년(?P<month>\d{1})월(?P<day>\d{2})일'),
                re.compile(r'(?P<year>\d{4})년(?P<month>\d{1})월(?P<day>\d{1})일')
            ]
            
            for regex in regexes:
                match = regex.search(command)

                if match:
                    today = datetime.date.today()

                    year = match.group('year')
                    month = match.group('month')
                    day = match.group('day')

                    if len(month) == 1:
                        month = '0' + month

                    if len(day) == 1:
                        day = '0' + day

                    dateString = year + '-' + month + '-' + day

                    return Menu.getMenuByDate(dateString)

            regexes = [
                re.compile(r'(?P<month>\d{2})월(?P<day>\d{2})일'),
                re.compile(r'(?P<month>\d{2})월(?P<day>\d{1})일'),
                re.compile(r'(?P<month>\d{1})월(?P<day>\d{2})일'),
                re.compile(r'(?P<month>\d{1})월(?P<day>\d{1})일'),
            ]

            for regex in regexes:
                match = regex.search(command)

                if match:
                    today = datetime.date.today()

                    year = str(today.year)
                    month = match.group('month')
                    day = match.group('day')

                    if len(month) == 1:
                        month = '0' + month

                    if len(day) == 1:
                        day = '0' + day

                    dateString = year + '-' + month + '-' + day

                    return Menu.getMenuByDate(dateString)

            regexes = [
                re.compile(r'(?P<day>\d{2})일'),
                re.compile(r'(?P<day>\d{1})일')
            ]

            for regex in regexes:
                match = regex.search(command)

                if match:
                    today = datetime.date.today()

                    year = str(today.year)
                    month = str(today.month)
                    day = match.group('day')

                    if len(month) == 1:
                        month = '0' + month

                    if len(day) == 1:
                        day = '0' + day

                    dateString = year + '-' + month + '-' + day

                    return Menu.getMenuByDate(dateString)      
                
            return onFail('날짜를 정확히 말해 임마')
        elif "하이" in command:
            return Greeting.echo("하이")
        elif "헬로" in command:
            return Greeting.echo("헬로")
        elif "hello" in command:
            return Greeting.echo("hello")
        elif "hi" in command:
            return Greeting.echo("hi")
        elif "봇하" in command:
            return Greeting.echo("유하")
        elif "안녕" in command:
            return Greeting.echo("안녕")

        return onFail('무슨 말인지 모르겠는걸')
            
            
            

            
            

    