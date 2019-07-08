import requests
from bs4 import BeautifulSoup

text = open('VexG.html', encoding="utf8")
# print(text)
soup = BeautifulSoup(text, "lxml")

res = requests.get('https://www.google.com/search?q=vexanium成因塊')
res.encoding = "utf-8"
print(res.text)
soupR = BeautifulSoup(res.text, "lxml")

leng = len(soup.get_text())
srT = soupR.get_text()
sT = soup.get_text()

tag = ".BNeawe"
tag1 = ".iUh30"
for d in soupR.select('{}'.format(tag)):
    print(d.get_text())










# tagO = ".無糖"
# resO = requests.get('http://pala.tw/class-id-example/')
# soupO = BeautifulSoup(resO.text, "lxml")

# for drinkO in soupO.select('{}'.format(tagO)):
#     print(drinkO.get_text())
