import urllib.request
import re
'''
爬虫网易音乐 ，获取音乐信息
'''
response = urllib.request.urlopen("http://music.163.com/#/discover/toplist")
html = response.read().decode('utf-8') #网页 字符串形式
str = html.replace("\r\n","")
findall = re.findall(r"<title>.*</title>", str)
re_findall = re.findall("\\.m-table-rank",findall)
print(re_findall)
print(findall[0].replace(r"<title>","").replace(r"</title>",""))






