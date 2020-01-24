# pip install requests BeautifulSoup4

import json, requests 

url = "https://ssgfoodingplus.com/fmn101.do?goTo=todayMenuJson"

mealId = "mealId=&"
mealTypeCd = "mealTypeCd=&"
storeCd = "storeCd=05600&"
cafeCd = "cafeCd=01&" 
menuDate = "menuDate=2020-01-22" # 얘가 변수

query = {
    "mealId" : "",
    "mealTypeCd" : "",
    "storeCd" : "05600",
    "cafeCd" : "01",
    "menuDate" : "2020-01-22"
}

res = requests.post(url, data=query)

# print(url)
# print(query)
rows = res.json()["result"]

breakfasts = []
lunches = []
dinners = []

for row in rows:
    mealType = row['meal_type_nm']
    if mealType == "조식":
        breakfasts.append(row)
    elif mealType == "중식":
        lunches.append(row)
    elif mealType == "석식":
        dinners.append(row)

# for i in range(len(str1)):
#     for j in str1[i]:
#         print(str1[i][j])
print("--------------------------------------------------------------------------------------------------------------------------")
print(breakfasts)
print("--------------------------------------------------------------------------------------------------------------------------")
print(lunches)
print("--------------------------------------------------------------------------------------------------------------------------")
print(dinners)
print("--------------------------------------------------------------------------------------------------------------------------")

# print(len(str1))