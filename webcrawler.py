import requests
from bs4 import BeautifulSoup

searchTargets = ["vexanium", ""]

#If there are multiple keywords, put "%20" as space
searchRequestDefault = "https://www.google.com/search?q="
searchRequestBaidu = "https://www.baidu.com/s?wd="
searchRequestGoogle = "https://www.google.com/search?q="

#Search Get URL Parser
def searchParser(keyword, engine):
    flag = 1
    for i in range(len(keyword)):
        if keyword[i] == " ":
            s = keyword.split(" ")
            jString = "%20".join(s)
            flag = 0
    if flag:
        jString = keyword
    req = ""
    if engine == 1:
        req = searchRequestGoogle + jString
    elif engine == 2:
        req = searchRequestBaidu + jString
    else:
        req = searchRequestDefault + jString

    return req

def crawl(keyword, engine, target):
    searchURL = searchParser(keyword, engine)
    print(searchURL)
    res = requests.get(searchURL)
    page = BeautifulSoup(res.text, "lxml")
    matchHeader = []
    matchNumber = 0

    for element in page.select('{}'.format(".LC20lb")):
        print(element)
        if target in element:
            matchHeader.append(element.get_text())
            matchNumber = matchNumber + 1
            print(element)
    
    print(matchNumber)


print(searchParser("Vex PP", 1))
crawl("Vexanium", 1, "price")

#tag = input("請輸入定位元素，class前面加上.，id前面加上# ")
#tag = ".半糖 去冰 珍珠 奶茶"
tag = ".author-nickname"
res = requests.get('https://www.google.com/search?q=%E6%96%B0%E7%AF%87%E7%AB%A0+Vexanium%E6%88%90%E5%9B%A0%E5%9D%97&safe=strict&ei=LrgiXZ60CIi5rQGW9JTQCA&start=20&sa=N&filter=0&ved=0ahUKEwieg_i2sKTjAhWIXCsKHRY6BYo4ChDw0wMIlQE&biw=1280&bih=578')
print(res.encoding)
res.encoding = 'utf-8'
print(res.encoding)

soup = BeautifulSoup(res.text, "lxml")
print(soup)
#print(soup)

for d in soup.select('{}'.format(tag)):
    print(d.get_text())