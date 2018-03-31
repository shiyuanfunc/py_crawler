import urllib.request
import re

response = urllib.request.urlopen("https://wwww.baidu.com")
html = response.read().decode('utf-8')
print(type(response.read()))
str = html.replace("\r\n","")
findall = re.findall(r"<title>.*</title>", str)
print(findall[0].replace(r"<title>","").replace(r"</title>",""))






