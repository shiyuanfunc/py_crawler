import requests
import urllib
from bs4 import BeautifulSoup
import re

url = "https://search.jd.com/Search?keyword=%E7%AC%94%E8%AE%B0%E6%9C%AC&enc=utf-8&wq=%E7%AC%94%E8%AE%B0%E6%9C%AC&pvid=bd1fb25566024baba545e03a626dbf6d"
respone = urllib.request.urlopen(url)
html = respone.read().decode('utf-8').replace("\r\n","");
soup = BeautifulSoup(html, "html.parser")
#print(html)

#find_all = soup.find_all('ul', class_='J_valueList v-fixed')
# soup_find_all = soup.find_all('div', attrs={'class':re.compile('p-img')})
# for i in soup_find_all:
#     print(i)
#     find_all = i.find_all('a')
#     for a in find_all:
#         print(a.get('href'))
#         print(a.get('title'))
#print(soup_find_all)

find_all = soup.find_all('li', attrs={'class': 'gl-item'})
for li in find_all:
    #print(li)
    price = li.find('div', class_='p-price').find('i')
    url = li.find('div', class_='p-img').find('a').get('href')
    url = str(url)
    if url.startswith("//"):
        print(price)
        print(url)
        print("------------------")
