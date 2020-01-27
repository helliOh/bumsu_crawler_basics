### Basics of Cralwer with Python
---

#### INDEX
---
getting start crawling with python easy peasy 

#### CONTENTS
---

1. /tutorials
    -   crawler
		- app
			- app.py : Crawling data and send it to channel
		- api-crawl.py : Crawling data directly from API server (CSR applications)
		- headless.py : Image or AJAX based sites crawling
		- html.py : Crawling html, parsing logic would be required (SSR applications)
	-	slack
		- bot.py : simple version of sending message
2. /crawler_http : Django web application, checkout the image below

#### Django Structure

Image will be upload in here

#### REQUIREMENTS
---

##### 3.6 <= Python 
In console, type python --version  
In case you already downloaded the python but cannot execute it  
check out the environment variables  
  
##### 60 <= Chrome  
you can check following link [my version](chrome://version/)  
  
##### Chromedriver  
  
check out the version then download proper file in the link below   
[download chromedriver](https://chromedriver.chromium.org/downloads)  
  
Slack :: Account and API Access Token  
[Slack API](https://api.slack.com/)  
  
##### Your Apps - OAuth & Permissions::  
  
Configure the access permission of your app  
Hit the create button, Copy your access key and paste into token, which is variable name, in slack/bot.py  
  
##### Guide line

Shell
```shell
pip install -r requirements.txt
```

config/env.json
```javascript
{
	"SLACK_BOT_TOKEN" : "FOO",
	"SLACK_DEFAULT_CHANNLER" : "BAR"
}
```

Shell
```bash
django-admin runserver

Or

python manage.py runserver
```

If commands don't work, check out the version of your python.  
If you are working on Linux, you might be needed to add package repository, which is dead snake, before  
using the install command of package manager  
  
Q : PIP doesn't work well  
A : First of all, check out the python version django has some dependency on it.  

Q : PIP still doesn't work well :(
A : If you have multiple version of python without virtual environment, pip might not install  
the package in the right version of python library. specify the version of it using manual command.  

```bash
(any version >= 3.6)
python3.8 -m pip install -r requirements.txt
python3.7-m pip install -r requirements.txt
python3.6-m pip install -r requirements.txt
```

Q : Bot doesn't work
A : Make sure that you invited the bot first. If problem goes on, check out you have right API token,  
event subscriber.

#### External Source
---

- API 호출 함수 이름 : fnRefreshMealTypeList()
- API 주소 : https://ssgfoodingplus.com/fmn101.do?goTo=todayMenuJson

- 데이터 원형 : mealId=&mealTypeCd=&storeCd=05600&cafeCd=01&menuDate=2020-01-22

#### Data Structure
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
