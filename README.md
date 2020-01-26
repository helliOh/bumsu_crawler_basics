### Basics of Cralwer with Python
---

#### INDEX
---
getting start crawling with python easy peasy 

#### CONTENTS
---

1. /slack
    -   bot.py
2. /crawler
    -   chromedriver.exe
    -   headless.py
    -   html.py
3. /crawler
    -   django app structure
    	- django app - fetch : fetch raw data
	- django app - slack_api : send message to slack(token needed)

#### API STRUCTURE
```mermaid
	mainApp-->fetchApp;
	mainApp-->slackApiApp;
	ssgfooding-->fetchApp;
	ssgfooding-->slackApiApp;
	slackBotApi-->slackApiApp;
```

#### REQUIREMENTS
---

3.6 <= Python 
In console, type python --version  
In case you already downloaded the python but cannot execute it  
check out the environment variables  
  
60 <= Chrome  
you can check following link [my version](chrome://version/)  
  
Chromedriver  
  
check out the version then download proper file in the link below   
[download chromedriver](https://chromedriver.chromium.org/downloads)  
  
Slack :: Account and API Access Token  
[Slack API](https://api.slack.com/)  
  
Your Apps - OAuth & Permissions::  
  
Configure the access permission of your app  
Hit the create button, Copy your access key and paste into token, which is variable name, in slack/bot.py  
  
Packages  
  
-   slack/bot.py : pip install slack slackclient
    -   API access token is necessary
-   crawler/headless.py : pip install selenium
    -   Right version of chromedrive should be in this directory
-   crawler/html.py : pip install request BeautifulSoap4

UPDATES
---

- API 호출 함수 이름 : fnRefreshMealTypeList()
- API 주소 : https://ssgfoodingplus.com/fmn101.do?goTo=todayMenuJson

- 데이터 원형 : mealId=&mealTypeCd=&storeCd=05600&cafeCd=01&menuDate=2020-01-22

데이터 as dict.
---
```
{
	"key" : null,
	"mealTypeCd"=&
	"storeCd" : 05600&
	"cafeCd" : 01,
	"menuDate" : 
}
```
