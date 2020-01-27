#pip install requests BeautifulSoup4

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.naver.com")  
DOM = BeautifulSoup(html, "html.parser")

au_item = DOM.find_all("li", class_="au_item")
at_item = DOM.find_all("li", class_="at_item")

for elem in au_item:
    print("au")
    print(elem)
    
for elem in at_item:
    print("at")
    print(elem)

print("parse ended")

