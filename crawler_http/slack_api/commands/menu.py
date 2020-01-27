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

def fetch(date):
    url = "https://ssgfoodingplus.com/fmn101.do?goTo=todayMenuJson"
    print(date)

    query = {
        "mealId" : "",
        "mealTypeCd" : "",
        "storeCd" : "05600",
        "cafeCd" : "01",
        "menuDate" : date
    }

    res = requests.post(url, data=query)

    rows = res.json()["result"]

    breakfasts = []
    lunches = []
    dinners = []

    todayMenu = {
        "breakfast" : [],
        "lunch" : [],
        "dinnerKR" : [],
        "dinnerEN" : []
    }

    for row in rows:
        mealType = row['meal_type_nm']
        if mealType == "조식":
            todayMenu["breakfast"].append(row)
        elif mealType == "중식":
            todayMenu["lunch"].append(row)
        elif mealType == "석식":
            dinnerType = row['dinner_type_nm']

            if dinnerType == "일반식(한식)":
                todayMenu["dinnerKR"].append(row)

            elif dinnerType == "일반식(양식)":
                todayMenu["dinnerEN"].append(row)

    return todayMenu

def sendMessage(data):
    (breakfasts, lunches, dinnersKR, dinnersEN) = data["breakfast"], data["lunch"], data["dinnerKR"], data["dinnerEN"]

    count = 1
    breakfastContents = " ```오늘의 조식\n\n"

    for breakfast in breakfasts:
        breakfastContents = breakfastContents + "\t" + str(count) + ". " + breakfast["if_menu_nm"] + "\n"
        count = count + 1

    count = 1
    breakfastContents = breakfastContents + " ``` "
    lunchContents = " ```오늘의 중식\n\n"

    for lunch in lunches:
        lunchContents = lunchContents + "\t" + str(count) + ". " + lunch["if_menu_nm"] + "\n"
        count = count + 1

    lunchContents = lunchContents + " ``` "
    dinnerContents = " ```오늘의 석식\n"

    count = 1
    dinnerContents = dinnerContents + "\n\t한식 \n\n"

    for dinnerKR in dinnersKR:
        dinnerContents = dinnerContents + "\t\t" + str(count) + ". " + dinnerKR["if_menu_nm"] + "\n"
        count = count + 1

    count = 1
    dinnerContents = dinnerContents + "\n\t 양식 \n\n"

    for dinnerEN in dinnersEN:
        dinnerContents = dinnerContents + "\t\t" + str(count) + ". " + dinnerEN["if_menu_nm"] + "\n"
        count = count + 1

    dinnerContents = dinnerContents + " ``` "

    client = WebClient(token=token)
    response = client.chat_postMessage(channel=channelName, text=breakfastContents)
    response = client.chat_postMessage(channel=channelName, text=lunchContents)
    response = client.chat_postMessage(channel=channelName, text=dinnerContents)

    return data

class Menu:
    def todayMenu():
        """View function for home page of site."""
        today = datetime.date.today()
        data = fetch(str(today))

        return sendMessage(data)

    def tomorrowMenu():
        """View function for home page of site."""
        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(days=1)
        data = fetch(str(tomorrow))

        return sendMessage(data)
        
    def getMenuByDate(dateString):
        """View function for home page of site."""
        data = fetch(str(dateString))
        return sendMessage(data)
        