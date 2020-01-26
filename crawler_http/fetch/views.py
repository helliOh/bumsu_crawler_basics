# -*- coding: utf-8 -*-
import datetime
import requests

from django.http import JsonResponse
from rest_framework.exceptions import ValidationError, ParseError

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

# list commands
def index(request):
    """View function for home page of site."""
    res = [
        {
            "command" : "오늘 메뉴"
        },
        {
            "command" : "내일 메뉴"
        },
        {
            "command" : "메뉴"
        }
    ]
    
    # Render the HTML template index.html with the data in the context variable
    return JsonResponse(
        res,
        json_dumps_params={'ensure_ascii': False},
        content_type="application/json; encoding=utf-8",
        safe=False
        )

def todayMenu(request):
    """View function for home page of site."""
    today = datetime.date.today()
    
    data = fetch(str(today))
    res = data
    # Render the HTML template index.html with the data in the context variable
    return JsonResponse(
        res,
        json_dumps_params={'ensure_ascii': False},
        content_type="application/json; encoding=utf-8",
        safe=False
        )

def tomorrowMenu(request):
    """View function for home page of site."""
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)

    data = fetch(str(tomorrow))
    res = data
    
    # Render the HTML template index.html with the data in the context variable
    return JsonResponse(
        res,
        json_dumps_params={'ensure_ascii': False},
        content_type="application/json; encoding=utf-8",
        safe=False
        )

def getMenuByDate(request, dateString):
    """View function for home page of site."""
    data = fetch(str(dateString))
    res = data
    
    # Render the HTML template index.html with the data in the context variable
    return JsonResponse(
        res,
        json_dumps_params={'ensure_ascii': False},
        content_type="application/json; encoding=utf-8",
        safe=False
        )
    
    

