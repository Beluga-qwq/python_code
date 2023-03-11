import requests
x= requests.get('https://www.bilibili.com/')
print(x.text+'/n')