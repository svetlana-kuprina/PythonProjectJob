# Дан следующий синхронный код, который загружает текстовую информацию с трёх различных URL-адресов по порядку:

import requests

def get_data(url):
    response = requests.get(url)
    return response.text

data1 = get_data('<http://example.com/data1>')
data2 = get_data('<http://example.com/data2>')
data3 = get_data('<http://example.com/data3>')

print(data1)
print(data2)
print(data3)

async def get_data(url):
    response = requests.get(url)
    return response.text